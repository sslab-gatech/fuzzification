#!/usr/bin/env python2
import os
import sys
import string

from pwn import *
from executor import *
from tqdm import tqdm

context.arch = 'amd64'

TARGET = sys.argv[1]
"""
if "_" in TARGET:
  OUTPUT = TARGET.split("_")[0]+"_rop"
elif ".all" in TARGET:
  OUTPUT = TARGET.split(".")[0]+"_all"
else:
  OUTPUT = TARGET+".rop"
"""
OUTPUT = sys.argv[2]

JMPTABLE = "jtable"
GADGET = "ropgadget"
GADGET_TEMP = "ropgadget_temp"
GADGET_GENERATOR = "./genrop.sh"
SIGNAL_FUNC = "\<dummy\>"
SIGNAL_FUNC2 = "\<dummy2\>"
JMP_SIGNATURE = "\xee\xee\xee\xee\xee\xee\xee\xee\xdd\xdd\xdd\xdd\xdd\xdd\xdd\xdd"
TMP_OBJDUMP = "/tmp/objdmp"

PRE_INST_SIZE = 8 * 2 # I added 8 function-calls (8*2)
GROUP_TABLE_SIZE = 100
JMP_TABLE_SIZE = 900
ADDR_SIZE = 8 # we are assuming x64

# this doesn't work => entire size maybe vary for each location
INSERTED_FUNC = 0x412830 - 0x4127fb
LIMIT = 5000

# calc offset from <dummy> to 4th <markfunc>
def ret_dummy_to_mark (pn):
  cmd = "objdump -M intel -d %s > %s" % (pn, TMP_OBJDUMP)
  os.system(cmd)
  out = {}
  
  with open(TMP_OBJDUMP, 'r') as f:
    lines = f.readlines()
    found = False
    markfunc = 0
    addr_dummy = None
    addr_markfunc = None
    
    for x in xrange(len(lines)):      
      line = lines[x]    
      
      if "call" in line and "<dummy>" in line:
        addr_dummy = hex(int(line.split(":")[0].strip(), 16)) 
        #addr_dummy_int = int(line.split(":")[0].strip(), 16)
        found = True

      if found and "call" in line and "<markfunc>" in line:
        markfunc = markfunc + 1
      
      if found and "call" in line and "<markfunc>" in line and markfunc == 4:
        found = False
        markfunc = 0
        addr_markfunc = int(line.split(":")[0].strip(), 16)
        out[addr_dummy] = addr_markfunc - int(addr_dummy, 16)

  return out

def correct_objdump_addr(pn):
  out = []
  cmd = "objdump -d %s" % pn
  output = execute(cmd, capture=True).split("\n")
  for line in output:
    if ":" in line and all(c in string.hexdigits for c in line.split(":")[0].strip()):

      addr = int(line.split(":")[0].strip(), 16)
      out.append(addr)

  return out

def identify_markfunc_addr (pn):
  out = []
  cmd = "objdump -d %s |grep -B 4 dummy2|grep mark" % (pn)
  output = execute(cmd, capture=True).split("\n")
  
  for line in output:
    if ":" in line and all(c in string.hexdigits for c in line.split(":")[0].strip()):
      addr = int(line.split(":")[0].strip(), 16)
      out.append(addr)

  return out
  

# TODO. need to handle binary patch nicely
def correct_div_addr(pn):

  out = []
  # for test
  return out

  # afl-clang-fast patch
  cmd = "objdump -d %s|grep \"be ee 00 00 00\"" % pn

  output = execute(cmd, capture=True).split("\n")
  for line in output:
    if ":" in line and all(c in string.hexdigits for c in line.split(":")[0].strip()):

      addr = int(line.split(":")[0].strip(), 16)
      out.append(addr)

  return out

def ret_jmptable_addr(pn):
  cmd = "nm %s |grep %s" % (pn, JMPTABLE)
  output = execute(cmd, capture=True).split(" ")[0]
  return hex(int(output, 16))
  
def correct_gadget(pn):
  print "  >> patch.py: generating ROPgadget (takes time)"
  cmd = "%s %s" % (GADGET_GENERATOR, pn)
  output = execute(cmd)

  cmd = "head -n %d %s > %s" % (LIMIT, GADGET_TEMP, GADGET)
  os.system(cmd)

def patch_point(pn):

  """ parsing these lines
  4006df:       e8 cc 02 00 00          callq  4009b0 <dummy>
  400763:       e8 48 02 00 00          callq  4009b0 <dummy>
  4007e9:       e8 c2 01 00 00          callq  4009b0 <dummy>
  """

  outarry = []
  cmd = "objdump -d %s |grep %s" % (pn, SIGNAL_FUNC)
  out = execute(cmd, capture=True).split("\n")

  for line in out:
    if ":" in line and "call" in line:
      addr = hex(int(line.split(":")[0].strip(), 16) - 0)
      outarry.append(addr)
  return outarry

def patch_end_point(pn):

  """ parsing these lines
  4006df:       e8 cc 02 00 00          callq  4009b0 <dummy>
  400763:       e8 48 02 00 00          callq  4009b0 <dummy>
  4007e9:       e8 c2 01 00 00          callq  4009b0 <dummy>
  """

  outarry = []
  cmd = "objdump -d %s |grep %s" % (pn, SIGNAL_FUNC2)
  out = execute(cmd, capture=True).split("\n")

  for line in out:
    if ":" in line and "call" in line:
      addr = hex(int(line.split(":")[0].strip(), 16) - 0)
      outarry.append(addr)
  return outarry

def init_jmptable(size):
  out = []
  for x in range(size):
    out.append(p64(0))
  return out

class Patch:
  "Patch binary"

  def __init__(self, elf_pn):
    self.elf_pn = elf_pn
    self.elf = ELF(self.elf_pn)
    self.valid_addr = correct_objdump_addr(self.elf_pn)
    self.div_addr = correct_div_addr(self.elf_pn)

    self.patch_point = patch_point(self.elf_pn)
    self.patch_end_point = patch_end_point(self.elf_pn)
    self.markfunc = identify_markfunc_addr(self.elf_pn)  # list
    self.jmptable = init_jmptable(JMP_TABLE_SIZE+GROUP_TABLE_SIZE)
    self.dummy_to_mark = ret_dummy_to_mark(self.elf_pn)

    # generate gadget file (External)
    correct_gadget(self.elf_pn)

    self.gadget_dict = self.ret_gadget(GADGET)

    # get the jmp-table address
    self.jump_baseaddr = int(ret_jmptable_addr(self.elf_pn), 16)
    self.group = self.gadget_group()

    self.group_metadata = {} # for each group, store groupnum and size
    self.jmp_metadata = {}


  def find_distance_of_loc(self, addr):
    distance = 0x100

    for key in self.patch_end_point:
      if key > addr:
        if int(key, 16) - int(addr,16) < distance:
          distance = int(key, 16)- int(addr, 16)
    return hex(distance+5)


  def find_closest_div_addr(self, addr):
    
    distance = 0x1000
    minimum = None

    #print self.div_addr
    #exit()
    for key in self.div_addr:
      if key < int(addr, 16):        
        if int(addr,16) - key < distance:
          distance = int(addr, 16) - key
          minimum = key
    #return hex(int(addr, 16) - distance)
    if minimum is not None:
      return hex(minimum)
    else:
      return hex(-30)

  def find_closest_gadget_addr(self, addr):
    keys = self.gadget_dict.keys()
    distance = 0x100

    for key in keys:
      if key > addr:
        if int(key, 16) - int(addr,16) < distance:
          distance = int(key, 16)- int(addr, 16)
    return hex(int(addr, 16) + distance)

  def ret_gadget(self, pn):
    print "  >> patch.py: classifying collected gadget (takes time)"
    out = {}
    f = open(pn, 'r')
    lines = f.readlines()

    for line in tqdm(lines, mininterval=5):
      if "0x" in line and ":" in line and "ret " not in line:
        #print line
        addr = int(line.split(":")[0].strip(), 16)
        address = hex(addr)
        gadget = line.split(":")[1].strip()

        if addr in self.valid_addr:
          out[address] = gadget
    return out
  
  def patch_jmp_table(self, jmpdata):
    f = open (TARGET, 'rb')
    binary_data = f.read()
    f.close()
    
    offset = binary_data.find(JMP_SIGNATURE)
    if offset == -1:
      print "cannot find the jump-table signature"

    else:
      f = open (OUTPUT, 'r+b')    
      f.seek(offset)
      f.write(jmpdata)
      f.close()

  def gadget_group(self):
    group = {}

    for addr in self.patch_point:
      g_addr = self.find_closest_gadget_addr(addr)
      #print g_addr

      #if g_addr in self.gadget_dict.keys():
      gadget = self.gadget_dict[g_addr]

      if gadget not in group.keys():
        group[gadget] = [g_addr]
      else:
        group[gadget].append(g_addr)
    return group

  def generate_table(self):
    """
    1. generate group-table
    2. generate jmp-table
    3. do not patch now => we will patch after dump from pwnlib
    """
    gt_writing_index = 0
    jt_writing_index = GROUP_TABLE_SIZE

    # for addresses in the same group (gadget)
    counter = 0
    for key in self.group.keys():

      # wrting current group table information first
      self.jmptable[gt_writing_index] = p64(self.jump_baseaddr \
        + (jt_writing_index * ADDR_SIZE))
      
      # modify group metadata 
      self.group_metadata[key] = [gt_writing_index, len(self.group[key])]

      # increase gt index by one (we can increase more)
      gt_writing_index = gt_writing_index + 1

      # writing actual gadget into table
      counter = counter + 1

      for jmpindex in range(len(self.group[key])):

        if jt_writing_index > 998:
          break
        self.jmptable[jt_writing_index] = p64(int(self.group[key][jmpindex], 16))

        # increase index
        jt_writing_index = jt_writing_index + 1

  def patch_binary_split(self):
    """
    1. compare 0 with ret valuie
    2. if eq to 0 ==>  jmp to original execution (jmp 11 bytes)
    3. else       ==> just random thing (ret or error)
    """
    
    jmp_assembly = """
    cmp eax, 0x0
    je {addr}
    test eax, eax
    jmp {addr2}
    nop
    nop
    jmp rsi
    """

    # we modify right after the mark function
    # read return value and conditional jump
    for addr in self.markfunc:
      emit_asm = jmp_assembly.replace("{addr}", hex(addr+0x10))
      emit_asm = emit_asm.replace("{addr2}", hex(addr+0x11))
      asmcode = asm(emit_asm, vma=addr)

      self.elf.write(addr, asmcode)      

    # NOTE: good to go?
    patch.elf.save(OUTPUT)
    os.chmod(OUTPUT, 0755)

    jmpdata = ''.join(str(e) for e in self.jmptable)
    self.patch_jmp_table(jmpdata)


    
  def patch_binary(self):
    """
    for each patch location, (we are patching each function-end)
    1. what is my group? 
    2. resolve group-table (maybe 100 entries)
    3. resolve jmp-table  (maybe 900 entries)
    4. previous code should be remained
    5. patch for each location

    after iteration,
    1. dump the patch to binary
    2. apply additional patch on jmp-table 

    jmp-table reference

    get the index of group table
           --------------------------
           |                        |
          [i]                       v
    [ group-table ] [           jmp-table        ] [gadget]
                                    |                ^
                                    |                |
                                    ------------------
    """

    for location in tqdm(self.patch_point, mininterval=3):

      patchdata = ""
      gadget_addr = self.find_closest_gadget_addr(location)
      
      # return distance of function calls
      dist = self.find_distance_of_loc(location)

      """
      if int(location, 16) - int(div_addr, 16) > 0x20:
        print "too far"
        continue
      """
      
      key = self.gadget_dict[gadget_addr]
      group_index, group_size = self.group_metadata[key]
      group_addr = self.jmptable[group_index]

      # we can select one entry of group table before the assembly
      # and we can also patch it
      # find pre-epilogue instructions and store as binary-data
      mid_data_size = int(gadget_addr,16) - int(location, 16)      
      if mid_data_size - int(dist,16) < 0:
        print "prevent wrong memory reference"
        continue

      # for afl, I added offset(of 5)
      

      mid_data = self.elf.read(int(location, 16)+int(dist,16), mid_data_size - int(dist,16))
      #print len(mid_data)
      
      """
      0x400a09 <main+345>: call   0x400a20 <slp>
      ==========================================
               <find this one>
                      |
                      |
                      v
      0x400a0e <main+350>: mov    eax,ebx
      0x400a10 <main+352>: add    rsp,0x38
      ==========================================
      0x400a14 <main+356>: pop    rbx
      0x400a15 <main+357>: pop    rbp
      0x400a16 <main+358>: ret    
      """

      div_assembly = """
      mov edi, {1}
      """

      # we are free to use %rdi because of immediate function-call
      # [rsi+0] should use the same gadget group (choose from xor-args)
      # skip jmp rsi

      jmp_assembly = """
      mov edx, 0
      mov r9, rax
      mov rax, rdi
      mov ecx, {1}
      div ecx
      mov rax, r9
      mov edi, edx
      mov rsi, {2}
      imul edi, 8
      add rsi, rdi
      mov rsi, [rsi]      
      """

      # {1}: jmp table address 
      jmp_assembly = jmp_assembly.replace("{1}", str(group_size))
      jmp_assembly = jmp_assembly.replace("{2}", str(hex(u64(group_addr))))
      asm_data2 = asm(jmp_assembly)

      num_nop = self.dummy_to_mark[location] - len(asm_data2) -1
      asm_data2 += "\x90" * num_nop

      
      self.elf.write(int(location, 16), mid_data + asm_data2)
      ## end of for loop

    #NOTE: we are not generating file at this stage (but after branch_split)
    #patch.elf.save(OUTPUT)
    #os.chmod(OUTPUT, 0755)

    # Uncomment this. patching the jmp-table at the last moment
    #jmpdata = ''.join(str(e) for e in self.jmptable)
    #self.patch_jmp_table(jmpdata)

if __name__ == '__main__':
  patch = Patch(TARGET)

  print "[*] Generating table"
  patch.generate_table()

  print "[*] Patch the binary using rop-based approach"
  patch.patch_binary()

  print "[*] Patch the binary for branch_split"
  patch.patch_binary_split()