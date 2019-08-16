#!/usr/bin/env python2
import sys
import os
import shutil
import subprocess
import signal
from time import sleep
from threading import Timer

# load settings
from conf import *

# load local modules
sys.path.append('./util')
from measure import *
from normalbb import *
from measure_bb import *
from benchmark_eval import *

# load compile command
sys.path.append('../antifuzz-tutorial')
from build_template import COMMAND

### USER's configuration
# disable the below env-variable setting if you already make an environment
os.environ["AFL_PATH"] = os.path.abspath("../fuzzer/afl-2.51b-bbcheck")

#DELAYS         = [30,50,70,100]
DELAYS         = [300]
OVERHEAD       = [3]  # user can check different overhead budget
NON_VISIT_BUMP = 5
NON_VISIT_ANTI = 5
NON_VISIT_COV  = 5

NORMAL_COV     = 1 # for all fuzzifications
NORMAL_ANTI    = 5 # for all fuzzifications

INCLUDE_NON_VISIT = True
PROCESS_INCORRECT = True

### global variables
COMP_SCRIPT = COMMAND[SAMPLE]
FINAL_OUT = ""
LAST_DELAY = 0
LAST_RATIO = 0
HIGHEST_RATIO = -1
ORG_SIZE = os.path.getsize(os.path.join(SAMPLE_DIR, SAMPLE))
LOGFILE = "/tmp/.log_%s" % SAMPLE

def mkdirs(pn):
  try:
    os.makedirs(pn)
  except OSError as e:
    pass

def make_working_dir():
  os.makedirs(WORKING_DIR)
  
def make_bb_dir():
  os.makedirs(INFO_DIR)
  os.makedirs(CORRECT_BB_DIR)
  os.makedirs(INCORRECT_BB_DIR)

def prepare_fuzz_dir():
  os.system("rm -rf %s" % FUZZ_OUTPUT_DIR)
  os.makedirs(FUZZ_OUTPUT_DIR)  

def clean_up_working_dir():
  if os.path.exists(WORKING_DIR):
    shutil.rmtree(WORKING_DIR)

def clean_up_bb_dir():
  if os.path.exists(INFO_DIR):
    os.system("rm -rf %s" % INFO_DIR)

# deprecated
def make_llvmpass_so():
  build_dir = os.path.join(DELAYPASS, "build")
  os.system("cd %s; make clean; make" % (build_dir))    

def parse_command(cmd, target):
  tmp = cmd.split('[[')[1].split(']]')[0].strip()
  tmparr =  tmp.split(' ')
  out = []
  basename = []
  instname = []
  for item in tmparr:
    out.append(item.split('.o')[0])
    basename.append(os.path.basename(item))
    instname.append(item.split('.o')[0]+"_%s.o" % target)
  return out, basename, instname

def copy_and_inst(candidate, stage):
  os.system("cp %s %s" % ("factory/*.so", WORKING_DIR))
  os.system("cp %s%s %s" % (SCRIPTPASS, "/*.sh", WORKING_DIR)) 

  counter = 0
  for item in candidate:
    path = os.path.join(COMP_DIR, item+".o")
    os.system("cp %s %s" % (path, WORKING_DIR))

    # for instrumenting anti
    cmd = "cd %s;./make_%s.sh %s" % (WORKING_DIR, stage, os.path.basename(item))
    counter += 1
    os.system(cmd)

def makelog(c_overhead, s_overhead, stage):
  with open(LOGFILE, 'a') as f:
    msg = "%s: cpu overhead- %f, size overhead- %f\n" % \
      (stage, c_overhead, s_overhead * 100)
    f.write(msg)

def copy_back(candidate, instname):
  for i in range(len(candidate)):
    src = "%s.o" % candidate[i]

    # copy-back instrumented
    srcpath = os.path.join(WORKING_DIR, os.path.basename(instname[i]))
    dstpath = os.path.join(COMP_DIR, instname[i])
    os.system("cp %s %s" % (srcpath, dstpath))

  #copy collision_delays
  os.system("cp %s %s" % (DELAY_COLLISION+"/*.o", COMP_DIR))

  #copy delay_primitives
  os.system("cp %s %s" % (DELAY_USLP+"/*.o", COMP_DIR))

  #copy dummy_primitives
  os.system("cp %s %s" % (DEFENSE+"/*.o", COMP_DIR))

def prepare(compile=False):
  # compile llvm-pass and prepare dirs
  clean_up_working_dir()    
  make_working_dir()  
  if compile:
    make_llvmpass_so()

def print_comp_command(cmd, instname):
  head = cmd.split('[[')[0]
  tail = cmd.split(']]')[1]
  mid = ' '.join(instname)
  return head + " " + mid + " " + " " + DELAYOBJ+ " "+ tail

def ret_filename(delay, ratio):
  return "r"+str(ratio)+"_"+"d"+str(delay)

def dumpbb_tofile(bbs, addition=None):
  # dump BBs list to file (INST_BB)

  print "[*] Writing BBs to file"
  dummy = 0.001
  f = open(INST_TARGET, 'w')  
  for item in bbs:
    f.write(str(item)+","+str(dummy)+"\n")
  f.close()
  os.system("mv %s %s" % (INST_TARGET, WORKING_DIR))

  if addition is not None:    
    f2 = open(addition, 'w')
    for item in bbs:
      f2.write(str(item)+","+str(dummy)+"\n")
    f2.close()
    cmd = "mv %s %s" % (addition, WORKING_DIR)    
    os.system(cmd)

def fuzz_benchmark(delay, ratio, bin_pn):
  print "[*] Fuzzer performance for delay %s (ms) and %s (percent)" % (str(delay), str(ratio))
  prepare_fuzz_dir()

  kill = lambda process: process.send_signal(signal.SIGINT)
  AFL_FUZ_ABS = os.path.abspath(AFL_FUZ)
  cmd = "%s -i %s -o %s -t %s %s %s @@" % \
    (AFL_FUZ_ABS, FUZZ_INPUT_DIR, FUZZ_OUTPUT_DIR, FUZZ_TIMEOUT, bin_pn, ARGS)
  os.system("timeout --signal=SIGINT %ds %s" % (TOTAL_FUZZ_TIMEOUT, cmd))  

def analyze_fuzz_perf(delay, ratio):
  reportfile = os.path.join(FUZZ_OUTPUT_DIR, "fuzzer_stats")

  execs_per_sec = "N/A"
  paths_total = "N/A"

  if os.path.exists(reportfile):
    f = open(reportfile, 'r')
    lines = f.readlines()
    f.close()

    for line in lines:
      if "execs_per_sec" in line:
        execs_per_sec = line.split(':')[1].strip()
      if "paths_total" in line:
        paths_total = line.split(':')[1].strip()

    report = "D(%s)/R(%s)  execs_per_sec: %s, paths_total: %s\n " \
      % (str(delay), str(ratio), execs_per_sec, paths_total)
    print report
    global FINAL_OUT
    FINAL_OUT += report

def compile_binary(targetname=None, library=False):
  # this is the normal path to compile one binary
  if library == False:
    cmd = print_comp_command(COMP_SCRIPT, instname)
    #print cmd
    print "cd %s;%s" % (COMP_DIR, cmd)
    os.system("cd %s;%s" % (COMP_DIR, cmd))

    if targetname is not None:
      print "mv %s %s" % (COMP_DIR+"/"+SAMPLE, COMP_DIR+"/"+targetname)
      os.system("mv %s %s" % (COMP_DIR+"/"+SAMPLE, COMP_DIR+"/"+targetname))
      return COMP_DIR+"/"+targetname

  # build library first then compile binary  
  else:
    cmd1 = print_comp_command(COMP_SCRIPT, instname)
    
    print "\n"+cmd1
    os.system("cd %s;%s" % (COMP_DIR, cmd1))

    print COMP_SCRIPT2
    os.system("cd %s;cd ..;%s" % (COMP_DIR, COMP_SCRIPT2))

    if targetname is not None:
      print "mv %s %s" % (COMP_DIR+"/"+SAMPLE, COMP_DIR+"/"+targetname)
      os.system("mv %s %s" % (COMP_DIR+"/"+SAMPLE, COMP_DIR+"/"+targetname))
      return COMP_DIR+"/BUILD"+targetname

def run_build(targetname, delay_val, option, show=False):
  #print targetname, delay_val, option  
  cmd = "cd %s ;%s %s %s %s" % (COMP_DIR, "./build-%s.sh" % SAMPLE, \
    targetname, delay_val, option)  
  if show is True:
    print cmd
  os.system(cmd)    
  return COMP_DIR+"/"+targetname

def fname_minus(filename):
  items = filename.split("_")
  value = int(items[2].split('r')[1])
  if value > 0:
    value = value-1
  return items[0] + "_" + items[1] + "_" + "r" + str(value) + "_" + items[3]

def update_oripn(fname):  
  target_pn = os.path.join(SAMPLE_DIR, SAMPLE)  # test/binaries
  cmd = "cp %s %s" % (fname, target_pn)
  os.system(cmd)

def store_generated(target, stage):
  print " - Storing generated"
  target_pn = ret_output_name(stage)
  output_pn = os.path.join(OUTPUT_DIR, SAMPLE, target_pn)
  
  mkdirs(OUTPUT_DIR)
  mkdirs(OUTPUT_DIR+"/"+SAMPLE)

  cmd = "cp %s %s" % (target, output_pn)
  os.system(cmd)
  return output_pn

def speedbump(_delay=None, _ratio=None):
  print "\n===================="
  print "SpeedBump"
  print "===================="
  found_bump = False  
  stage = "bump"
  prev_fname = ""
  prev_T = ""
  overhead = OVERHEAD[0]

  # generate initial baseline binary
  fname = "%s_temp" % SAMPLE
  T = run_build(targetname = fname, delay_val = "0", option="init")   
  update_oripn(T)
  

  # try instrumentation within overhead budget
  if _delay is None:    
    global FINAL_OUT
    global HIGHEST_RATIO
    global LAST_DELAY
    global LAST_RATIO
    global ORG_SIZE

    f.write("OVERHEAD %d of threshold\n" % overhead)
    print "OVERHEAD %d of threshold\n" % overhead
    
    FINAL_OUT += "OVERHEAD %d of threshold\n" % overhead          
    prev_overhead = 0.0
    success_delay = 0
    
    init_bb(pn=T)

    # try delays specified in config
    # just normal cases (first run)
    for delay in DELAYS:
      normal_ratio =-1
      
      while True:
        normal_ratio +=1
        print "=" * 50
        print "[*] prepare delay: we are using %d ms delay" % delay
        print "  >> Current percentage of normal BBs: %d" % normal_ratio
        
        # return instrumentation candidate
        print "  >> return bbs profile information"
        bbs = ret_bbs(normal_ratio, non_visit=INCLUDE_NON_VISIT, \
          non_visit_ratio=NON_VISIT_BUMP, process_incor=PROCESS_INCORRECT)
        #print len(bbs)

        filename = ret_filename(delay, normal_ratio)
        DELAYOBJ = "delay_" + str(delay) + ".o"

        print "[*] Dump profiled information"
        prepare(compile=False)
        dumpbb_tofile(bbs)
        candidate, basename, instname = parse_command(COMP_SCRIPT, "bump")        

        print "[*] Copy and do instrumentation"
        copy_and_inst(candidate, "bump")
        copy_back(candidate, instname)

        fname = "%s_d%s_r%s_o%s" % \
          (SAMPLE, str(delay), str(normal_ratio), str(overhead))

        #print fname, delay
        print "[*] Build new test binary"
        T = run_build(targetname = fname, delay_val = str(delay), option="slow")
        current_overhead = ret_overhead(delay, normal_ratio, overhead) 
        print "  >> Test overhead:", current_overhead

        # if current overhead exceeds ==> quit
        if overhead < current_overhead:  
          print "[*] Found case which exceeds overhead budget"
          found_bump = True        
          FINAL_OUT += "Delay: %sms, inst_percentage: %d, filename: %s \n" \
            % (delay, normal_ratio-1, prev_fname)
          f.write("Delay: %sms, inst_percentage: %d, filename: %s \ncp %s temp\n" % \
            (delay, normal_ratio-1, fname_minus(fname), prev_fname))

          # if there was success case
          if prev_T != "":            
            store_generated(prev_T, stage)
            print FINAL_OUT
            break

          else:
            print " >> We couldn't make the bump work, please try to reduce sleep size"
            break

        # if we can go further, store current information
        else:
          print "[*] found case within overhead budget"
          prev_fname = fname
          prev_T = T
          prev_overhead = current_overhead
          LAST_DELAY = delay
          LAST_RATIO = normal_ratio
          if normal_ratio >= HIGHEST_RATIO:            
            HIGHEST_RATIO = normal_ratio        

  # This branch is for applying more components (e.g., trap or pandora)
  # so we assume that we already know delay and ratio.
  else:
    # since makeanti compile source with branch_Trap and anti-analysis
    # we can use it for all instrumentation
    print "[*] speedbump for makeall (all fuzzifications)"
    fname = "%s_temp" % SAMPLE    
    T = run_build(targetname = fname, delay_val = str(0), option="makeanti") 

    init_bb(pn=T)
    SAMPLE_PN = os.path.join(SAMPLE_DIR, SAMPLE)
    os.system("cp %s %s" % (T, SAMPLE_PN))
    
    store_for_benchmark(T)

    # we should put generated binary for BB
    found_bump = True
    prepare(compile=False)
    print "[*] Dump profiled information"

    ### for next instrumentations ###
    bbs = ret_bbs(NORMAL_COV, non_visit=INCLUDE_NON_VISIT, \
          non_visit_ratio=NON_VISIT_COV, process_incor=True) 
    dumpbb_tofile(bbs, addition="bb_cov")

    bbs = ret_bbs(NORMAL_ANTI, non_visit=INCLUDE_NON_VISIT, \
          non_visit_ratio=NON_VISIT_ANTI, process_incor=True)
    dumpbb_tofile(bbs, addition="bb_anti")
    ###    

    bbs = ret_bbs(_ratio, non_visit=INCLUDE_NON_VISIT, \
          non_visit_ratio=NON_VISIT_BUMP, process_incor=PROCESS_INCORRECT)
    dumpbb_tofile(bbs)
    
    candidate, basename, instname = parse_command(COMP_SCRIPT, "bump") 
    print " >> candidates:", len(candidate)
    print " >> Speedbump for all instrumentations with delay %d ratio %d" % (_delay, _ratio)    
    
    copy_and_inst(candidate, "bump")
    copy_back(candidate, instname)

    fname = "%s_d%s_r%s_o%s" % \
          (SAMPLE, str(_delay), str(_ratio), str(overhead))
    prev_fname = fname

    #print fname, delay
    print "[*] Run_build (for all fuzzifications)"
    T = run_build(targetname = fname, delay_val = str(_delay), option="slow")         

  # this is the first time of storing  
  gen_pn = os.path.join(COMP_DIR, prev_fname)  
    
  if found_bump == True:
    print " >> Measuring overhead again"
    c_overhead, s_overhead = _ret_overhead(gen_pn)
    print " >> %s: %f cpu, %f size overhead" % (stage, c_overhead, s_overhead)
  
  return LAST_DELAY, LAST_RATIO, prev_fname, c_overhead, s_overhead

def prepare_rop():
  os.system("cp llvm_pass/%s/script/genrop.sh %s" % ("trap", WORKING_DIR))
  os.system("cp llvm_pass/%s/patch.py %s" % ("trap", WORKING_DIR))

def copy_back_target(src, target):
  os.system("cp %s %s" % (src, target))
  bname = os.path.basename(src)
  return bname

def patch_rop(target, output):
  os.system("cd %s; python patch.py %s %s" % (WORKING_DIR, target, output))

  return os.path.join(WORKING_DIR, output)

def coverage():
  print "\n===================="
  print "BranchTrap"
  print "===================="
  stage = "coverage"

  # 1) prepare
  print "[*] prepare the trap (collect another profiling)"
  bbs = ret_bbs(NORMAL_COV, non_visit=INCLUDE_NON_VISIT, \
          non_visit_ratio=NON_VISIT_COV, process_incor=True) 
  #print "we will try %d basicblocks" % len(bbs)
  prepare(compile=False) 
  prepare_rop()    # copy necessary stuff
  dumpbb_tofile(bbs)  
  candidate, basename, instname = parse_command(COMP_SCRIPT, "coverage")        

  # 2) instrument pandora and rop
  print "[*] instrument huge_branches and rop"
  copy_and_inst(candidate, "coverage")
  copy_and_inst(candidate, "rop")
  copy_back(candidate, instname)
  
  fname = SAMPLE + "_coverage"
  T = run_build(targetname = fname, delay_val = str(0), option="coverage") 
  T = copy_back_target(T, WORKING_DIR)
  T = patch_rop(T, SAMPLE+"_rop")  # assume it is at WORK_DOR/%target_coverage  

  store_generated(T, stage)

  fname = SAMPLE + "_rop"
  compiled_pn = os.path.join(WORKING_DIR, fname)
  copy_back_target(compiled_pn, COMP_DIR)  
  
  gen_pn = os.path.join(COMP_DIR, fname)
  c_overhead, s_overhead = _ret_overhead(gen_pn)  

  return c_overhead, s_overhead

def makeall():
  stage = "all"

  # 1) compile src with anti-taint + branch-trap (generate new-object)
  #run_build(targetname = "%s_anti" % SAMPLE, delay_val = str(0), option="makeanti") 

  # 2) BUMP: generate intermediate objects from speedbump
  speedbump(_delay=LAST_DELAY, _ratio=LAST_RATIO)  

  # apply coverage and anti-sym  
  candidate, basename, instname = parse_command(COMP_SCRIPT, "all")  

  # 3) COVERAGE and ANTI-ANALYSIS, then build
  print "[*] Copy_and_inst for ALL"
  copy_and_inst(candidate, "all") # make_coverage.sh + make_rop.sh + make_anti.sh ==> result to _anti
  copy_back(candidate, instname)

  fname = SAMPLE + "_%s" % stage + "_temp"
  T = run_build(targetname = fname, delay_val = str(LAST_DELAY), option="all")
  T = copy_back_target(T, WORKING_DIR)

  # 3-1) patch binary for rop-based approach  
  prepare_rop()  
  fname = SAMPLE + "_%s" % stage
  T = patch_rop(T, SAMPLE+"_all")
  out_pn = store_generated(T, stage)

  # measure overhead
  gen_pn = os.path.join(COMP_DIR, fname)
  c_overhead, s_overhead = _ret_overhead(out_pn)

  return c_overhead, s_overhead

def _ret_overhead(gen_pn):  
  current_overhead = ret_overhead(0,0,0, inst_pn = gen_pn)
  target_pn = os.path.join(OUTPUT_DIR, SAMPLE)
  newfile_size = os.path.getsize(gen_pn)
  s_overhead = float(newfile_size) / float(ORG_SIZE)

  return current_overhead, s_overhead

def ret_output_name(stage):
  return SAMPLE + "_" + stage

def anti_analysis():
  stage = "anti"

  # start from new object (makeanti)
  run_build(targetname = "%s_anti" % SAMPLE, delay_val = str(0), option="makeanti") 

  # init_bb again(do another bb profiling)
  # because we re-generate binary at this stage
  # from above we generate executable file: e.g., readelf_anti 
  anti_pn = os.path.join(COMP_DIR, SAMPLE+"_anti")
  init_bb(pn=anti_pn)

  # FIXME: input of normal ratio
  # FIXME: should not recompile for different generation
  bbs = ret_bbs(NORMAL_ANTI, non_visit=INCLUDE_NON_VISIT, \
          non_visit_ratio=NON_VISIT_ANTI, process_incor=True)
  
  print " >> compiling binary"
  prepare(compile=False)

  print " >> dump basicblock profile"  
  dumpbb_tofile(bbs)
  candidate, basename, instname = parse_command(COMP_SCRIPT, "anti")

  print " >> copy_and_inst"
  copy_and_inst(candidate, "anti")
  copy_back(candidate, instname)

  fname = SAMPLE + "_anti"
  T = run_build(targetname = fname, delay_val = str(0), option="anti") 
  store_generated(T, stage)

  # measure overhead
  gen_pn = os.path.join(COMP_DIR, fname)
  c_overhead, s_overhead = _ret_overhead(gen_pn)

  return c_overhead, s_overhead

def init_bb(pn=None):
  print "[*] Initialize BasicBlock profiling result"
  clean_up_bb_dir()
  make_bb_dir()
  generate_bb_info(pn)

def store_for_benchmark(ori_pn):
  target = os.path.join(SAMPLE_DIR, SAMPLE) 
  os.system("cp %s %s" % (ori_pn, target))

def backup_original():
  #ori_pn = os.path.join(SAMPLE_DIR, SAMPLE)
  ori_pn = os.path.join(COMP_DIR, SAMPLE)
  store_generated(ori_pn, "ori") # backup the file to output dir
  store_for_benchmark(ori_pn)

if __name__ == '__main__':
  print "\n===================================================="
  print "Generate multiple binary and measure the performance"
  print "===================================================="

  # prepare dirs
  # get the total_bb and copy to sample dir
  os.system("rm -f %s" % LOGFILE)
  os.system("rm -f %s" % "/tmp/logfile")
  prepare(compile=False)
  f = open(TARGET_FILES, 'w')
  
  init_bb()
  backup_original()  
  
  if not os.environ.has_key("DEBUG"):
    # 1. BUMP: apply speedbump (orig => bump)  
    bump_depay, bump_ratio, fname, c_overhead, s_overhead = speedbump()
    print 
    print "*"* 50
    print "[*] SpeedBump: cpu overhead %f, size overhead %f" % (c_overhead, s_overhead)
    makelog (c_overhead, s_overhead, "bump")    

    # 2-1. COVERAGE: branchtrap (orig => trap)
    # 2-2. COVERAGE: pandora (orig => pandora)
    # 2-3. COVERAGE: rop-based file transformation
    # 2.4. COVERAGE: branch_split  
    c_overhead, s_overhead = coverage()
    print 
    print "*"* 50
    print "[*] BranchTrap: cpu overhead %f, size overhead %f" % (c_overhead, s_overhead)
    makelog (c_overhead, s_overhead, "coverage")
    
    # 3-1. ANTI-ANALYSIS: anti-sym
    # 3-2. ANTI-ANALYSIS: anti-taint-analysis
    c_overhead, s_overhead = anti_analysis()
    print 
    print "*"* 50
    print "[*] ANTI: cpu overhead %f, size overhead %f" % (c_overhead, s_overhead)
    makelog (c_overhead, s_overhead, "anti")

  # 4. ALL: apply all (orig => all)  
  #print "*"* 50
  #LAST_RATIO = 7  # for test
  #LAST_DELAY = 80 # for test
  #print "  >> delay is", LAST_DELAY
  #print "  >> ratio is", LAST_RATIO

  print 
  print "*"* 50
  print "[*] All Fuzzifications in one binary"
  c_overhead, s_overhead = makeall()
  print "[*] ALL: cpu overhead %f, size overhead %f" % (c_overhead, s_overhead)
  makelog (c_overhead, s_overhead, "all")
