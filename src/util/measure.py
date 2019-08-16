"""
This script provide "ret_elapsetime()" and this function measures
total execution time for the taget application
"""

import os, sys
import time
import commands

sys.path.append('../')
from conf import *

# set timeout
TIMEOUT = 10

# setup dir according to the target
COR_DIR = os.path.join(SAMPLE_DIR, SAMPLE, CORRECT_INPUT)
INCOR_DIR = os.path.join(SAMPLE_DIR, SAMPLE, INCORRECT_INPUT)
SAMPLE_PN = os.path.join(SAMPLE_DIR, SAMPLE, SAMPLE)
CORBB_DIR = os.path.join(SAMPLE_DIR, SAMPLE, CORRECT_BB_DIR)

def cleanup_dirs(path, ext):
  for root, dirs, files in os.walk(path):
    for currentFile in files:
      if currentFile.lower().endswith(ext) is True:
        os.remove(os.path.join(root, currentFile))

def load_filelist_from_dir(dirname, onlyfile = True):
  "Get all files end without extension in directory"
  extension_path = []
  for root, dirs, files in os.walk(dirname):
    for filename in files:
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

def run_showmap(target, input, output):  
  command = "%s -o %s -- %s %s  >/dev/null 2>&1" % (SHOWMAP, output, target, input)
  commands.getoutput(command)

def ret_tmpoutput(target):
  return os.path.join(TMP_DIR, target)

def _run_mapcomp(filelist):
  for item in filelist:
    basename = os.path.basename(item)
    dirname = os.path.dirname(item)
    #print item
    run_showmap(T, item, os.path.join(dirname, basename+BB_EXTENTION))  

def run_mapcomp():
  corlist = load_filelist_from_dir(COR_DIR, onlyfile = False)  
  incorlist = load_filelist_from_dir(INCOR_DIR, onlyfile = False)
  _run_mapcomp(corlist)
  #_run_mapcomp(incorlist)

def move_bb(pn):
  #print "mv %s %s" % (COR_DIR+"/*.bb", CORBB_DIR)
  os.system("mv %s %s  >/dev/null 2>&1" % (COR_DIR+"/*.bb", CORBB_DIR))

def ret_elapsetime():
  starttime = time.time()
  cleanup_dirs(SAMPLE_DIR, ".bb")
  cleanup_dirs(SAMPLE_DIR, ".bb.2")

  global T
  T = ret_target(SAMPLE_PN, ARGS)
  run_mapcomp()
  cleanup_dirs(SAMPLE_DIR, ".bb")
  cleanup_dirs(SAMPLE_DIR, ".bb.2")
  move_bb(SAMPLE_DIR)

  endtime = time.time()
  #print "Elased %s" % (endtime-starttime)
  return (endtime - starttime)
