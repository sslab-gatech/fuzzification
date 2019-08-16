import sys
import time

#from delaypassconf import *

sys.path.append('../')
from conf import *

FINAL_OUT = ""
TIMEOUT_EACH = "1"
ITERATION = 1
OUTPUT = "/tmp/normallog"

elapsed_normal = None
elapsed_inst = None

#BIN_DIR = "/tmp/dst2"

def load_filelist_from_dir(dirname, onlyfile = True):
  "Get all files end without extension in directory"
  extension_path = []
  for root, dirs, files in os.walk(dirname):
    for filename in files:
      if onlyfile:
        extension_path.append(filename)
      else:
        extension_path.append(root + "/" + filename)
  return extension_path

def ret_target(target, args):
  target = "%s %s " % (target, args)
  return target

def bench1():
  # first benchmark
  SAMPLE_DIR = "/data/sslab/anti-fuzz/sample"
  SAMPLE_PN = os.path.join("..", SAMPLE_DIR, SAMPLE, SAMPLE+"_ori")

  T = ret_target(SAMPLE_PN, ARGS)

  sample_pn = os.path.join(SAMPLE_DIR, SAMPLE, "test")
  filelist = load_filelist_from_dir(sample_pn, onlyfile = False)

  ITER = 10

  start = time.time()

  for x in range(ITER):
    for filename in filelist:
      print filename
      os.system("%s %s > /dev/null" % (T, filename))

  print "original"
  print time.time() - start
  org = float(time.time() - start)

  # original
  SAMPLE_PN = os.path.join("..", SAMPLE_DIR, SAMPLE, SAMPLE+"_slow")

  T = ret_target(SAMPLE_PN, ARGS)

  filelist = load_filelist_from_dir(sample_pn, onlyfile = False)

  start = time.time()

  for x in range(ITER):
    for filename in filelist:
      os.system("%s %s > /dev/null" % (T, filename))

  print "instrumented"
  print time.time() - start
  ist = float(time.time() - start)

  print "overhead = "
  print float((ist/org) -1)


def bench2(test=True):
  """ second benchmark """

  # test samples directory
  BIN_DIR = ""

  # target binary path
  #SAMPLE_DIR = "/data/fuzz/sample/binutils-2.25/binutils"
  #ORI_PN = "/data/sslab/anti-fuzz/sample/readelf/readelf_temp"
  #SAMPLE_DIR = 
  #ORI_PN = os.path.join()

  ORI_PN = os.path.join(SAMPLE_DIR, SAMPLE, SAMPLE)
  INST_PN = COMP_DIR + SAMPLE + "_d%d_r%d_o%d" % (delay, ratio, overhead)
  BIN_DIR = COR_DIR = os.path.join(SAMPLE_DIR, SAMPLE, "test")

  if test is True:
    filelist = load_filelist_from_dir(BIN_DIR, onlyfile = False)
    #print filelist

    for nonratio in NON_VISIT_RATIO:
      global FINAL_OUT
      FINAL_OUT += "\nNON_VISIT_RATIO: %d\n" % nonratio
      for delay in DELAYS:
        for ratio in RATIO:
          targetname = "%s_d%s_r%s_n%s" % (SAMPLE, str(delay), str(ratio), str(nonratio))
          #print "processing: %s" % targetname
          start = time.time()

          for filename in filelist:
            #print filename
            T = "%s/%s %s" % (SAMPLE_DIR, targetname, ARGS)
            timeout_cmd = "%s %ss" % ("timeout --signal=SIGINT", TIMEOUT_EACH)
            #os.system("%s %s %s > /dev/null" % (timeout_cmd, T, filename))
            #print "%s %s > /dev/null" % (T, filename)
            os.system("%s %s > /dev/null" % (T, filename))

          elapsed = time.time() - start          
          global elapsed_normal
          report = "D(%s)/R(%s) elapsed = %s, overhead = %s%%\n" \
            % (str(delay), str(ratio), str(elapsed), str(((elapsed/elapsed_normal) - 1) * 100))
          FINAL_OUT += report
    return ((elapsed/elapsed_normal) - 1) * 100

  # test on original
  else:
    #global FINAL_OUT
    FINAL_OUT += "\nOriginal bench\n"
    counter=0

    filelist = load_filelist_from_dir(BIN_DIR, onlyfile = False)
    #print filelist
    T = "%s %s" % (ORI_PN, ARGS)
    start = time.time()

    for filename in filelist:      
      timeout_cmd = "%s %ss" % ("timeout --signal=SIGINT", TIMEOUT_EACH)
      #os.system("%s %s %s > /dev/null" % (timeout_cmd, T, filename))
      os.system("%s %s > /dev/null" % (T, filename))
      counter += 1

    elapsed = time.time() - start
    elapsed_normal = elapsed
    report = "elapsed = %s\n" % str(elapsed)
    FINAL_OUT += report

def bench3(delay, ratio, overhead, inst_pn=None):
  """ third benchmark """

  # test samples directory
  global FINAL_OUT
  print " - Measuring overhead for %d times" % ITERATION

  # target binary path
  ORI_PN = os.path.join(SAMPLE_DIR, SAMPLE)  # just compiled
  if inst_pn is None:
    INST_PN = COMP_DIR +"/" + SAMPLE + "_d%d_r%d_o%d" % (delay, ratio, overhead)
  else:
    INST_PN = inst_pn
  BIN_DIR = CORRECT_INPUT # = os.path.join(SAMPLE_DIR, SAMPLE, "test")
  
  #global FINAL_OUT
  FINAL_OUT += "\nOriginal bench\n"

  filelist = load_filelist_from_dir(BIN_DIR, onlyfile = False)

  ###########################################
  # measure overhead of original binary
  print " |original measuring iteration|"  
  T = "%s %s" % (ORI_PN, ARGS)
  start = time.time()
  
  for x in range(ITERATION):    
    elapsed = 0
    for filename in filelist:
      timeout_cmd = "%s %s " % ("timeout", TIMEOUT_EACH)
      cmd = timeout_cmd + T
      if MID_ARGS == False:           
        os.system("%s %s 1> /dev/null 2> /dev/null" % (cmd, filename))
      else:
        os.system("%s %s %s 1> /dev/null 2> /dev/null" % (cmd, filename, DEFAULT_ARG))   
  elapsed_normal = time.time() - start
  report = "    original elapsed = %s\n" % str(elapsed)
  print "  >> original elapsed = %s" % str(elapsed_normal)
  FINAL_OUT += report

  ###########################################
  # measure overhead of instrumented binary
  print " |overhead measuring iteration|"
  T = "%s %s" % (INST_PN, ARGS)
  start = time.time()
  
  for x in range(ITERATION):
    
    for filename in filelist:            
      timeout_cmd = "%s %s " % ("timeout", TIMEOUT_EACH)
      cmd = timeout_cmd + T
      if MID_ARGS == False:   
        os.system("%s %s 1> /dev/null 2> /dev/null" % (cmd, filename))
      else:
        os.system("%s %s %s 1> /dev/null 2> /dev/null" % (cmd, filename, DEFAULT_ARG))

  elapsed = time.time() - start
  elapsed_inst = elapsed
  report = "elapsed = %s\n" % str(elapsed)
  print "  >> instrumented elapsed = %s" % str(elapsed)
  overhead = ((elapsed_inst/elapsed_normal) - 1) * 100
  FINAL_OUT += report  
  return overhead

def ret_overhead():
  bench2(test=False)
  FINAL_OUT = ""
  out = bench2(test=True)
  return out

# This is used by antifuzz_all.py
def ret_overhead(delay, ratio, overhead, inst_pn=None):
  out = bench3(delay, ratio, overhead, inst_pn)
  return out

def print_report():
  bench2(test=False)
  global FINAL_OUT
  FINAL_OUT = ""
  out = bench2(test=True)
  print FINAL_OUT

  f = open(OUTPUT, 'w')
  f.write(FINAL_OUT)
  f.close()

if __name__ == '__main__':
  #print_report()
  bench1()
