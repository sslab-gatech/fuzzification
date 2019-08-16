#!/usr/bin/env python2

"""
TODO:
1. auto-run target binary with correct input
2. yield statatistics about visited basicblock frequency
 - should return never-visited blocks as well
"""

import os
import sys
import operator
import time
import random
import commands

sys.path.append('..')
from conf import *

# set timeout
TIMEOUT = 10

COR_DIR = CORRECT_BB_DIR
INCOR_DIR = INCORRECT_BB_DIR
SAMPLE_PN = os.path.join(SAMPLE_DIR, SAMPLE)
FUZZ_BB = os.path.join(INFO_DIR, BB_NAME)
TOTAL_BB_FILE = os.path.join(INFO_DIR, TOTAL_BB)

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
  command = "%s -o %s -- %s %s > /dev/null" % (SHOWMAP, output, target, input)  
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
  _run_mapcomp(corlist)

# return non_visited basicblocks by specified ratio
def ret_total_bb(non_visit_ratio):
  out = []
  f = open(TOTAL_BB_FILE, 'r')
  lines = f.readlines()

  #total_len = len(lines)
  total_len=0
  for line in lines:
    if "IDID" in line:
      total_len += 1

  counter = 0
  threshold = int(float(total_len) * (float(non_visit_ratio) / 100.0))
  #print "  >> threshold (number of instrumentation): ", threshold
  #print "  >> total BBs", total_len
  #print "  >> non-visit_ratio", non_visit_ratio, "%"

  random.shuffle(lines)

  for line in lines:
    if counter > threshold:
      return out

    if 'IDID' in line:
      bb = int(line.split('-')[1].strip())
      out.append(bb)
      counter += 1
  return out

def load_bb_from_dir(dirname, onlyfile = True):
  "Get all basicblock files from the project directory"
  extension_path = []
  for root, dirs, files in os.walk(dirname):
    for filename in files:
      if onlyfile:
        if filename.endswith(BB_EXTENTION):
          extension_path.append(filename)
      else:
        if filename.endswith(BB_EXTENTION):
          extension_path.append(root + "/" + filename)
  return extension_path

# filelist => read each file => store set => union
def ret_union(list):
  tempout = []
  for filename in list:
    tempout.append(Set(parse_input(filename)))
  result = set().union(*tempout)
  return result  # union of set

def div_list_float(list, num):
  out = []
  for i in list:
    val = i / float(num)
    out.append(val)
  return out

def ret_bb_diff(lista, listb):
    seta = ret_union(lista)
    setb = ret_union(listb)
    out = seta - setb  # get the difference (naive approach)
    return out

def run_all_input():
  T = ret_target(SAMPLE_PN, ARGS)
  run_mapcomp()
  cleanup_dirs(SAMPLE_DIR, ".bb.2")

def val_from_dict(dic):
  "get value to list"

  out = []
  for i in range(len(dic)):
    out.append(dic[i][1])
  return out

def ret_sorted_dict(dic):
  return sorted(dic.items(), \
      key=operator.itemgetter(1), reverse=True)

def match_dict(list1, list2):
  out = []
  ratio = {} # will be sorted dict
  for x in range(len(list1)):
    id = list1[x][0]
    hitcount = list1[x][1]
    if id in list2.keys():
      out.append(list2[id])
      ratio[list1[x][0]] = (list1[x][1] / list2[id])
  return out, ratio

def not_match_dict(list1, list2):
  # find entry that is only in list2

  out = []
  ratio = []
  for x in range(len(list2)):
    id = list2[x][0]
    hitcount = list2[x][1]
    if id not in list1.keys():
      out.append(id)
      ratio.append(hitcount)
      #print id, hitcount

  return out, ratio

def dict_diff(dict1, dict2):
  out = {}
  keys = list(set(dict1)-set(dict2))
  for key in keys:
    out[key] = dict1[key]
  return out

def percent_dict(dic, total):
  totalval = 0.0
  out = {}
  for key in dic.keys():   
    totalval += dic[key] / float(total)
    out[key] = dic[key] / float(total)
  return out

# count basicblock visit numbers 
class StatBasicBlock:
  "Count BasicBlock hit frequency"

  def __init__(self, pn_elf, cor, incor):
    # to process sets
    self.elf = pn_elf
    self.cordir = cor
    self.incordir = incor

    #basicblock hit file (.bb)
    self.corbb_list = load_bb_from_dir(self.cordir, onlyfile = False)
    self.corbb_list_len = len(self.corbb_list)

    #basicblock hit from incor execution (.bb)
    self.incorbb_list = load_bb_from_dir(self.incordir, onlyfile = False)
    self.incorbb_list_len = len(self.incorbb_list)

    self.hitdict_nor = {} # for correct input
    self.hitdict_abnor = {} # for incorrect input
    self.sorted_bb_nor = {}
    self.sorted_bb_nor_per = {}
    self.hitdict_nor_per = {}
    self.incor_dict = {}

    self.hitdict_fuz = {}
    self.total_fuz_run = 1
    self.sorted_bb_fuz = {}
    self.sorted_bb_fuz_per = {}
    self.hitdict_fuz_per = {}

    self.total_bb_count_nor = 0
    self.total_bb_count_fuz = 0
  
  # parse_input (for for normal showmap) (normal execution)
  def parse_input_nor(self, file1):
    "read input from normal showmap BB"

    counter = 0
    # f1: BB from normal
    f = open(file1, 'r')
    f1 = f.readlines()
    f.close()

    for line in f1:
      inst_id = line.split(':')[0].lstrip('0')
      count = int(line.split(':')[1].strip(), 16)
      counter += count

      if inst_id in self.hitdict_nor.keys():
        self.hitdict_nor[inst_id] += count
      else:
        self.hitdict_nor[inst_id] = count
    #self.total_bb_count_nor = counter
    return counter

  # parse_input (for for normal showmap) (normal execution)
  def parse_input_abnor(self, file1):
    "read input from normal showmap BB"

    counter = 0
    hitdict_abnor = {}
    # f1: BB from normal
    f = open(file1, 'r')
    f1 = f.readlines()
    f.close()

    for line in f1:
      inst_id = line.split(':')[0].lstrip('0')
      count = int(line.split(':')[1].strip(), 16)
      counter += count

      if inst_id == '':
        continue

      if inst_id in hitdict_abnor.keys():
        hitdict_abnor[inst_id] += count
      else:
        hitdict_abnor[inst_id] = count
    #self.total_bb_count_nor = counter
    return hitdict_abnor

  # parse_input (fuzzer execution)
  def read_bbfile_fuz(self):
    "read input from fuzzer BB visit result"

    counter = 0
    data = open(FUZZ_BB, 'r').readlines()
    total_exec = int(data[0].split(': ')[1].strip(), 16)
    self.total_fuz_run = total_exec
    f1 = data[1:]
    for line in f1:
      inst_id = line.split(':')[0].lstrip('0')
      count = int(line.split(':')[1].strip(), 16) 
      counter += count

      if inst_id in self.hitdict_fuz.keys():
        self.hitdict_fuz[inst_id] += count
      else:
        self.hitdict_fuz[inst_id] = count

    self.sorted_bb_fuz = sorted(self.hitdict_fuz.items(), \
      key=operator.itemgetter(1), reverse=True)

    self.total_bb_count_fuz = counter

  def sort_all(self):
    self.sorted_bb_fuz = sorted(self.hitdict_fuz.items(), \
      key=operator.itemgetter(1), reverse=True)    
    self.sorted_bb_nor = sorted(self.hitdict_nor.items(), \
      key=operator.itemgetter(1), reverse=True)    

  def sort_all_per(self):
    self.sorted_bb_fuz_per = sorted(self.hitdict_fuz_per.items(), \
      key=operator.itemgetter(1), reverse=True)    
    self.sorted_bb_nor_per = sorted(self.hitdict_nor_per.items(), \
      key=operator.itemgetter(1), reverse=True)    

  def read_bbfile_nor(self, process_incor = False):
    incor_dict = {}

    for filename in self.corbb_list:
      counter = self.parse_input_nor(filename)
      self.total_bb_count_nor += counter

    # 1) get the incor set 2) calc incor-cor
    if process_incor == True:
      for filename in self.incorbb_list:
        incor_dict = self.parse_input_abnor(filename)
        #print incor_dict
      for key in incor_dict.keys():
        if key not in self.hitdict_nor.keys():
          #print "Incorrect %d" % int(key, 16)
          self.hitdict_nor[key] = 0
          self.incor_dict[key] = 0

    self.sorted_bb_nor = sorted(self.hitdict_nor.items(), \
      key=operator.itemgetter(1), reverse=True)

    #print self.sorted_bb_nor

def div_list(lista, listb):
  assert (len(lista) == len(listb))
  out = []
  for x in range(len(lista)):
    out.append( lista[x] / listb[x])
  return out

def store_sorted_dic(_dict, percentage=100, head=False):  
  disp_len = float(len(_dict)) * float(percentage/100.0)
  #print "len: %s" % str(disp_len)
  #print len(_dict)
  #print disp_len
  counter = 0
  
  #f = open(INST_TARGET, 'w')
  out = []
  if disp_len < 0.00001:
    print "[*] zero, so no BBs from normal execution"
    return out

  for k,v in sorted(_dict.items(), key=operator.itemgetter(1), reverse=head):
    counter += 1
    if k is '':
      continue
    
    #print "%d, %f" % (int(k,16), v * 1000)
    #f.write("%d, %f\n" % (int(k,16), v * 1000))
    out.append(int(k,16))
    
    if counter > disp_len:
      #f.close()
      return out
  return out

def print_dict_for_inst(_dict, num):
  for i in range(num):
    print int(_dict[i][0], 16), int(_dict[i][1])

def ret_bbs(ratio, non_visit=False, non_visit_ratio=100, process_incor=False):
  # return least visited basicblocks for instrumentation
  # ratio: (1~4% from the whole blocks), values is percentage 
  # non_visit: include basicblock informatio which has not visited

  b = StatBasicBlock(SAMPLE_PN, CORRECT_BB_DIR, INCORRECT_BB_DIR)
  b.read_bbfile_nor(process_incor)
  b.hitdict_nor_per = percent_dict(b.hitdict_nor, b.total_bb_count_nor)
  b.sort_all_per()

  # partial executed (1% ~ xx%)
  out = store_sorted_dic(b.hitdict_nor_per, percentage=ratio) # display least visited bb from normal execution
  
  # total executed
  out2 = store_sorted_dic(b.hitdict_nor_per, percentage=100) # display least visited bb 

  # error-handling
  out3 = store_sorted_dic(b.incor_dict, percentage=100)
  
  # Do not consider non-visited basicblock
  if not non_visit:
    return out
    
  # Consider non-visited basicblock
  else:    
    total = ret_total_bb(non_visit_ratio)
    print "  >> non-visited (by ratio of %d): " % non_visit_ratio, len(total)
    print "  >> total visited: ", len(out2)
    out_set = set(out2)
    total_set = set(total)
    diff = total_set - out_set
    result = out + out3 + list(diff)  # we consider visited (e.g., 2% of visited) + non-visited
        
    return result

  #val_list1 = val_from_dict(b.sorted_bb_nor) # return sortedlist from dict

if __name__ == '__main__':

  # starttime
  starttime = time.time()

  # first run for generating bb-info for each input  
  #run_all_input()
  
  # merge and sort the normal execution BB-list
  b = StatBasicBlock(SAMPLE_PN, COR_DIR)
  b.read_bbfile_nor()
  b.read_bbfile_fuz()
  
  # make percentage scale
  b.hitdict_nor_per = percent_dict(b.hitdict_nor, b.total_bb_count_nor)
  b.hitdict_fuz_per = percent_dict(b.hitdict_fuz, b.total_bb_count_fuz)
  b.sort_all_per()

  store_sorted_dic(b.hitdict_nor_per, 10) # display least visited bb from normal execution
  
  # normal execution against fuzzer
  val_list1 = val_from_dict(b.sorted_bb_nor) # return sortedlist from dict
  val_list2, _ = match_dict(b.sorted_bb_nor, b.hitdict_fuz_per)   # find match against first argument  

  d = DrawLine("file1", [val_list1[0:300], val_list2[0:300]], \
    ylabel="visit count", xlabel="n-th BB",
    legend=["normal", "fuzzer"])
  d.draw()

  # fuzzer against normal execution
  val_list1 = val_from_dict(b.sorted_bb_fuz) # return sortedlist from dict
  val_list2, ratio = match_dict(b.sorted_bb_fuz, b.hitdict_nor_per)   # find match against first argument  
  ratio = ret_sorted_dict(ratio)
  
  d = DrawLine("file2", [val_list1[0:300], val_list2[0:300]], \
    ylabel="visit count", xlabel="n-th BB",
    legend=["fuzzer", "normal"])
  d.draw()

  # find basicblocks that executed only in fuzzer (not percent)  
  #var_list, hitcount = not_match_dict(b.hitdict_nor, b.sorted_bb_fuz)   # find not-match against first argument  
  var_list, hitcount = not_match_dict(b.hitdict_nor, b.sorted_bb_fuz)   # find not-match against 

  # for drawing count (not percentage)
  #val_list1 = div_list_float(val_list1, b.corbb_list_len)
  #val_list2 = div_list_float(val_list2, b.total_fuz_run)  

  """ fuzzer only
  fuzz_only_dic = dict_diff(b.hitdict_fuz, b.hitdict_nor)
  sort_dic = val_from_dict(ret_sorted_dict(fuzz_only_dic))
  sort_list = div_list_float(sort_dic, b.total_fuz_run)

  d = DrawLine("file", [sort_list], \
    ylabel="visit count", xlabel="n-th BB",
    legend=["fuzzer"])
  d.draw()
  """

  endtime = time.time()
  print "Elapsed %s" % (endtime - starttime)
