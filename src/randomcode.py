#!/usr/bin/env python2
import os, sys
import string
import random
import shutil
import time
import fileinput
import subprocess
import commands
from threading import Timer

#from executor import execute
from conf import *

# set up delay target
#DELAYS = [10,20,30,40,50,60,70,80,90, 100, 200, 300, 400, 500] # miliseconds
DELAYS = [1,2,3] # miliseconds 
OFFSET = 0.2 # i.e., we allow maximum 20% 

COMPILER = os.path.join(MOD_AFL, "afl-clang-fast")
WORKING_DIR = "./.csmith"

#user can set up custom probability table
# CSMITH_COMMAND = "./csmith --concise --no-safe-math --no-hash-value-printf  \
#                  --max-funcs {0} --no-builtins --no-checksum --no-arrays    \
#                  --no-compound-assignment --no-embedded-assigns             \
#                  --no-const-pointers --no-global-variables --no-longlong    \
#                  --no-pointers --max-array-dim 1 --max-array-len-per-dim 2  \
#                  --max-expr-complexity 2 --max-pointer-depth 1              \
#                  --max-struct-fields 2 --max-union-fields 2 --no-bitfields  \
#                  --no-comma-operators --no-compound-assignment              \
#                  --no-inline-function --no-structs --no-unions              \
#                  --probability-configuration util/prob -o {1}"
CSMITH_COMMAND = "./csmith --concise --no-safe-math --no-hash-value-printf  \
                 --max-funcs {0} --no-builtins --no-checksum --no-arrays    \
                 --no-compound-assignment --no-embedded-assigns             \
                 --no-const-pointers --no-global-variables                  \
                 --no-longlong --no-pointers --max-array-dim 1              \
                 --max-array-len-per-dim 2 --max-expr-complexity 2          \
                 --max-pointer-depth 1 --max-struct-fields 2                \
                 --max-union-fields 2 --no-bitfields --no-comma-operators   \
                 --no-compound-assignment --no-inline-function --no-structs \
                 --no-unions -o {1}"

GLOBAL_CHUNK = """
extern int global1;
extern int global2;
void change_global(int val)
{
    global2 = val;
}

"""

MAX_FUNC = 1000
TIMEOUT = 1
OUTPUT = "pass.o"
OUTPUT_PN = os.path.join(WORKING_DIR, OUTPUT)

FILEPREFIX = "delay_"
DEST = WORKING_DIR # temporary

gen_src = []
tmp_src = ""

def make_working_dir():
  os.makedirs(WORKING_DIR)

def clean_up_working_dir():
  if os.path.exists(WORKING_DIR):
    shutil.rmtree(WORKING_DIR)

def cp_header():
  os.system("cp %s/*.h %s" % (CSMITH_DIR, WORKING_DIR))
  os.system("cp %s/test.o %s" % (CSMITH_DIR, WORKING_DIR))

def random_string(size=6, chars=string.ascii_uppercase+string.ascii_lowercase):
  return ''.join(random.choice(chars) for _ in range(size))

def prepare():
  # remove working dir and make one
  clean_up_working_dir()
  make_working_dir()

  # copy header for compile
  cp_header()

def postprocess(pn, ranstr):  
  # change main function name with random_string name 

  for line in fileinput.input(pn, inplace=True):
    if "int main" in line:
      line = line.replace("main", "%s" % ranstr)
    sys.stdout.write(line)

  return 

def ch_main_arg(pn, argname, funcname):  
  # change main function name with random_string name 

  for line in fileinput.input(pn, inplace=True):
    if "int main" in line:
      line = line.replace("void", "%s" % argname)
      line = line.replace("main", "%s" % funcname)
    if "int print_hash_value = 0;" in line:
      #line = line.replace("0", "1")
      continue
    if "print_hash_value" in line:
      continue

    sys.stdout.write(line)

  return 

def inject_code_chunk(filename, _injectdata):
  f1 = open(filename, 'r')
  data = _injectdata + f1.read()
  f1.close()

  f2 = open(filename, 'w')
  f2.write(data)
  f2.close()

def gen_randomcodes(funcnum=1):
  for i in range(len(DELAYS)):
    print "[*] Finding delay primitives for %d(ms)." % (DELAYS[i])

    target_time = float(DELAYS[i]) / 1000
    offset = target_time * OFFSET

    while True:
      var = []

      output_name = FILEPREFIX+str(int(DELAYS[i]))
      var.append("%d" % MAX_FUNC)
      var.append(WORKING_DIR + "/" + output_name + ".c")
      
      cmd = CSMITH_COMMAND
      for j in range(2):
        cmd = cmd.replace("{%d}" % j, var[j])
        

      # generate random code compile via csmith      
      cmd = "timeout 2 %s " % cmd
      os.system(cmd)

      cmd2 = "cat %s |grep if|wc -l" % var[1]
      capt = commands.getoutput(cmd2)
      num_if = int(capt)

      # if we want many number of branches
      #if num_if < 2000:
      #  continue

      # compile as library
      tmp_src = var[1]
      #bin_compile(tmp_src)

      # change function name
      #random_name = random_string(size=8)
      #random_name = "slp" # let's fix for easy evaluation
      #postprocess(var[1], random_name) #arg: pn

      argname = "int print_hash_value"
      funcname = "slp"      
      ch_main_arg(var[1], argname, funcname)
      lib_compile(var[1], funcname)

      wrapper_compile(output_name)
      
      ##########################3
      # measure time
      pre_time = time.time()      

      kill = lambda process: process.kill()
      cmd = [WORKING_DIR+"/test"]      
      exec_sample = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
      my_timer = Timer(TIMEOUT, kill, [exec_sample])
 
      try:              
        my_timer.start()
        stdout, stderr = exec_sample.communicate()
      finally:        
        my_timer.cancel()        

      # compare time
      elapsed_time = time.time() - pre_time

      error = False
      try:
        commands.getoutput(cmd[0])
      except:
        error = True
      
      if error:
        print "ERROR"  
        continue

      """
      if stdout is not '':
        elapsed_time = float(stdout.split("\n")[len(stdout.split("\n"))-2])        
      else:
        continue
      """
      print " - Took %3.2f(ms). Our target is (%3.2f(ms) - %3.2f(ms))" % \
        (elapsed_time * 1000, (target_time-offset)*1000, (target_time+offset)*1000)
      if elapsed_time < target_time+offset or elapsed_time > target_time-offset:
        print "  ==> Found %d case" % DELAYS[i]
        print "  ==> Stored at %s" % (WORKING_DIR + "/" + output_name + ".c")
        inject_code_chunk(WORKING_DIR + "/" + output_name + ".c", GLOBAL_CHUNK)
        break

def wrapper_compile(name):
  """
  print "gcc -o %s %s %s" % (os.path.join(WORKING_DIR, "test"), \
                            os.path.join(WORKING_DIR, "test.o"),\
                            os.path.join(WORKING_DIR, name+".o"))
  """
  os.system("gcc -o %s %s %s" % (os.path.join(WORKING_DIR, "test"), \
                                 os.path.join(WORKING_DIR, "test.o"), \
                                 os.path.join(WORKING_DIR, name+".o")))

def bin_compile(name):
  base = os.path.splitext(name)[0]
  output = base
  commands.getoutput("gcc %s -o %s >/dev/null 2>&1" % (name, output))

def lib_compile(item, ranstr):
  base = os.path.basename(item).split(".c")[0]
  output = WORKING_DIR +"/" + base + ".o"
  commands.getoutput("gcc -c %s -o %s >/dev/null 2>&1" % (item, output))

if __name__ == '__main__':
  prepare()
  gen_randomcodes(funcnum=1)  
