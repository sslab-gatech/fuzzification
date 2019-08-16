INJECT1 = """struct addrarry{
          void *jt[1000];
} jtable = {0xeeeeeeeeeeeeeeee, 0xdddddddddddddddd};

void func1(void){
          int a=0;
}
"""

INJECT2 = """   jtable.jt[0] = &func1;
"""

import os, sys

filename = sys.argv[1]
inject2 = int( sys.argv[2] )

f = open(filename, "r")
contents = f.readlines()
f.close()

if "addr" not in contents[0]:
    contents.insert(inject2, INJECT2)
    contents.insert(0, INJECT1)

    f = open(filename, "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()

