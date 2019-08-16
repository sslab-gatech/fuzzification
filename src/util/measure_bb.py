#!/usr/bin/env python2
import os, sys
import time
import commands

sys.path.append('../')
from conf import *

# set timeout
TIMEOUT = 10

COR_DIR = CORRECT_INPUT
INCOR_DIR = INCORRECT_INPUT
SAMPLE_PN = os.path.join(SAMPLE_DIR, SAMPLE)
CORBB_DIR = CORRECT_BB_DIR
INCORBB_DIR = INCORRECT_BB_DIR

def cleanup_dirs(path, ext):
  for root, dirs, files in os.walk(path):
    for currentFile in files:
      if currentFile.lower().endswith(ext) is True:
        os.remove(os.path.join(root, currentFile))

def load_filelist_from_dir(dirname, onlyfile = True):
  "Get all files end without extension in directory"
  extension_path = []
  for root, dirs, files in os.walk(dirname):
    for filename in sorted(files):
      if onlyfile:
        if not filename.endswith(BB_EXTENTION):          
          extension_path.append(filename)
      else:
        if not filename.endswith(BB_EXTENTION):
          extension_path.append(root + "/" + filename)
  return extension_path

def ret_target(target, args):
  target = "%s %s " % (target, args)
  return target

def run_showmap(target, input, output, default=""):  
  command = "timeout 1 %s -m none -o %s -- %s %s %s 1> /dev/null 2> /dev/null" % (SHOWMAP, output, target, input, default)
  #command = "timeout 1 %s -m none -o %s -- %s %s %s " % (SHOWMAP, output, target, input, default)
  #print command
  try:
    commands.getoutput(command)
    cmd = "rm -f %s" % output
    f = open('/tmp/logfile', 'a')
    f.write(("rm -f %s" % input) + "\n")
    f.close()
  except:  
    #print "CRASH"
    pass

def ret_tmpoutput(target):
  return os.path.join(TMP_DIR, target)

def _run_mapcomp(filelist):
  # for each sample, run and collect coverage
  for item in filelist:
    basename = os.path.basename(item)
    dirname = os.path.dirname(item)
    if MID_ARGS == False:
      run_showmap(T, item, os.path.join(dirname, basename+BB_EXTENTION))  
    else:
      run_showmap(T, item, os.path.join(dirname, basename+BB_EXTENTION), DEFAULT_ARG)  

def mkdirs(pn):
  try:
    os.makedirs(pn)
  except OSError as e:
    pass

def run_mapcomp():
  corlist = load_filelist_from_dir(COR_DIR, onlyfile = False)  
  incorlist = load_filelist_from_dir(INCOR_DIR, onlyfile = False)

  # run and collect BB information
  _run_mapcomp(corlist)
  _run_mapcomp(incorlist)

def move_bb(pn):
  #print "mv %s %s" % (COR_DIR+"/*.bb*", CORBB_DIR)
  os.system("mv %s %s" % (COR_DIR+"/*.bb*", CORBB_DIR))

  #print "mv %s %s" % (INCOR_DIR+"/*.bb*", INCORBB_DIR)
  os.system("mv %s %s" % (INCOR_DIR+"/*.bb*", INCORBB_DIR))

def test():
  print SAMPLE

def generate_bb_info(pn=None):
  cleanup_dirs(SAMPLE_DIR, ".bb")
  cleanup_dirs(SAMPLE_DIR, ".bb.2")

  global T
  if pn is None:    
    T = ret_target(SAMPLE_PN, ARGS)  
  else:    
    T = ret_target(pn, ARGS) 
  
  run_mapcomp()  
  move_bb(SAMPLE_DIR)
  
def ret_exec_time():
  starttime = time.time()
  cleanup_dirs(SAMPLE_DIR, ".bb")
  cleanup_dirs(SAMPLE_DIR, ".bb.2")

  global T  
  T = ret_target(SAMPLE_PN, ARGS)
  run_mapcomp()
  cleanup_dirs(SAMPLE_DIR, ".bb.2")
  move_bb(SAMPLE_DIR)

  endtime = time.time()
  print "Elased %s" % (endtime-starttime)

"""
if __name__ == '__main__':
  
  starttime = time.time()
  cleanup_dirs(SAMPLE_DIR, ".bb")
  cleanup_dirs(SAMPLE_DIR, ".bb.2")

  T = ret_target(SAMPLE_PN, ARGS)
  run_mapcomp()
  cleanup_dirs(SAMPLE_DIR, ".bb.2")
  move_bb(SAMPLE_DIR)

  endtime = time.time()
  print "Elased %s" % (endtime-starttime)
  
"""