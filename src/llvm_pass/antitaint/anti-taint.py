#!/usr/bin/env python2
import sys
import os
import collections
import re
import commands
from random import randint

CTAGS = "/tmp/ctags"
INTERMEDIATE = "/tmp/intermediate"
INFORMATION_SINK = ["strcmp", "strncmp", "strchr", "strrchr"]
TEMPLATE_INT = """

//////////////// ANTI-TAINT-INT //////////////////
{type} {new_var}=0; 
if ({org_var} > 0 && {org_var} < 255)
{
    for ({type} i=0; i<=255; i++){
        if (i == {org_var}){
            {new_var} = i;
            break;
        }
    }
}
else {
    // give up anti-taint (to avoid long loop)
    // but we change anyway ...
    {new_var} = {org_var};
}
//////////////////////////////////////////////////
"""

TEMPLATE_STR = """

//////////////// ANTI-TAINT-STR //////////////////
char {new_var}[strlen({org_var})];
if (strlen({org_var}) < 30){    
    for (int i=0;i<strlen({org_var});i++){
        int ch=0;
        int temp = 0;
        int temp2 = 0;
        for (int j=0; j<8;j++){
            temp = {org_var}[i];
            temp2 = temp & (1<<j);
            if (temp2 !=0){
                ch |= 1<<j;
            }
        }
        {new_var}[i] = ch;
    }
}
else{    
    strncpy({new_var}, {org_var}, strlen({org_var}));
}
//////////////////////////////////////////////////
"""

def usage():
    print "python %s current_file.c new_file.c" % sys.argv[0]
    exit()

def word_in_list(_list, _word):
    if _word in _list:
        return True
    return False

def list_in_line(_list, line):    
    for word in _list:
        if word in line:
            return True, word
    return False, ""

def should_we_go(ratio):
    roll_dice = randint(1,100)
    if roll_dice < ratio:
        return True
    return False

def is_int_variable(line):
    items = line.split("\t")

    if len(items) > 4:
        # only consider variable and member
        if items[3] == 'v' or items[3] == 'm':
            if items[0] != '':
                return True, items[0], items[2]
    return False, "", ""

def ret_type(type_info):
    #if "*" in type_info:
    #    return False, ""
    
    if "unsigned int " in type_info:
        return True, "unsigned int"
    
    if "int " in type_info:
        return True, "int"

    #if "unsigned short" in type_info:
    #    return True, "unsigned short"

    return False, ""

# FIXME: so dirty ...
def if_condition(line):    
    if "if" in line and "(" in line and '\\' not in line \
        and "#" not in line and "else" not in line and \
        "NULL" not in line and " & " not in line:

        if line.strip().startswith("if"):            
            if line.count("(") ==1:
                return True

def no_switch_case(lines, x):
    boundary = 3
    if x>3:
        cur_lines = lines[x-boundary:x]
        for line in cur_lines:
            if "case" in line or "switch" in line or "for" in line:
                return False
    return True

class IntTaint(object):
    def __init__(self, filename, newfile, ratio):
        self.filename = filename
        self.newfile = newfile
        self.test_ctags()
        self.gen_ctags()
        self.types = self.get_types()
        self.gen_intermediate()
        self.mod_counter = 0
        self.ratio = ratio
        
    def test_ctags(self):
        cmd = "ctags"
        result = commands.getoutput(cmd)
        if "not found" in result:
            print "Error: please install ctags first!"
            print "e.g., $ sudo apt -f install ctags"
            exit()

    def ret_val_name(self):
        self.mod_counter += 1
        return "newvar_%d" % self.mod_counter

    def ret_mod_template_int(self, newvar, orgvar, type_info):
        out = TEMPLATE_INT.replace("{new_var}", newvar)
        out = out.replace("{org_var}", orgvar)
        out = out.replace("{type}", type_info)
        return out

    def ret_mod_template_str(self, newvar, orgvar):
        out = TEMPLATE_STR.replace("{new_var}", newvar)
        out = out.replace("{org_var}", orgvar)
        return out
   
    def has_target_sink(self, line):
        is_it, func_name = list_in_line(INFORMATION_SINK, line)
        if is_it and "if" in line \
            and "else" not in line:
            striped_line = line.replace(" ", "")
            
            if func_name+"(" in striped_line:
                operand = striped_line.split(func_name+"(")[1].split(",")[0]

                # make sure we don't change two times
                if line.count(operand) == 1:
                    return True, operand
        return False, ""

    def generate(self):
        
        gen_file = []
        # find place that we can modify safely
        with open(INTERMEDIATE, 'r') as f:
            lines = f.readlines()
            for x in xrange(len(lines)):
                modified_int = False
                line = lines[x]

                # for integer anti-taint-analysis                
                has_target, type_info, operand = self.target_var_in_dict(line)                
                if if_condition(line) and has_target and no_switch_case(lines,x):

                    # we can't apply them all, should roll a dice!
                    if should_we_go(self.ratio):
                        new_var = self.ret_val_name()
                        mod_template = self.ret_mod_template_int(new_var, operand, type_info)                   
                        line = mod_template + "\n" + line.replace(operand, new_var)

                # for string anti-taint-analysis
                """
                strategy#1: if comparison is on character, anti-taint
                strategy#2: information sink (strcmp, strncmp, ...)
                            we don't compare ctags type because we already know
                """

                # since there are not many sinks, we apply them all
                has_info_sink, operand = self.has_target_sink(line)
                if has_info_sink and not modified_int and no_switch_case(lines, x):
                    new_var = self.ret_val_name()
                    mod_template = self.ret_mod_template_str(new_var, operand)
                    line = mod_template + "\n" + line.replace(operand, new_var)

                gen_file.append(line.rstrip())
        
        out = "\n".join(gen_file)

        with open(self.newfile, 'w') as f:
            f.write(out)

    def target_var_in_dict(self, line):
        cond = line.replace("(", "")
        cond = cond.replace(")", "")
        cond = cond.replace("if", "")

        cond_list = []
        
        result = re.split('&& | \|\|', cond)
        if len(result) == 0:
            cond_list = [cond]
            cond_list = map(str.strip, cond_list)
        else:
            cond_list = result
            cond_list = map(str.strip, cond_list)
        
        operand_list = []
        for condition in cond_list:            
            result = re.split('== | > | < | !=', condition)
            operand_list = operand_list + result
        
        operand_list = map(str.strip, operand_list)
        
        # TODO: consider exclamation mark
        for operand in operand_list:
            contain_ext = "!" in operand
            if operand in self.types.keys() and line.count(operand) == 1 \
                and not contain_ext:
                return True, self.types[operand], operand

        return False, "", ""

    def gen_ctags(self):
        cmd = "ctags -f %s %s" % (CTAGS, self.filename)
        os.system(cmd)

    def get_types(self):
        """        
		m	member (of structure or class data)		
		v	variable
        """
        out = {}
        temp_list = []        
        duplicate_list = []
        with open(CTAGS, 'r') as f:
            lines = f.readlines()
            for line in lines:
                is_it, var_name, type_info = is_int_variable(line)
                if var_name != '':
                    temp_list.append(var_name)
            duplicate_list = [item for item, count in collections.Counter(temp_list).items() if count > 1]

        for line in lines:
            is_it, var_name, type_info = is_int_variable(line)
            is_acceptable, var_type = ret_type(type_info) 
            if var_name !='' and var_name not in duplicate_list and is_acceptable:
                out[var_name] = var_type        
                
        return out

    def gen_intermediate(self):
        with open(self.filename, 'r') as f1:
            lines = f1.readlines()
            out = ""
            for line in lines:
                if if_condition(line):
                    line = "\n" + line
                out += line

            with open(INTERMEDIATE, 'w') as f2:
                f2.write(out)                

def main():
    if len(sys.argv) < 2:
        usage()

    else:
        filename = sys.argv[1]
        new_filename = sys.argv[2]
        ratio = int(sys.argv[3])  # 1 to 100
        it = IntTaint(filename, new_filename, ratio)
        it.generate()
    
if __name__ == "__main__":
    main()
