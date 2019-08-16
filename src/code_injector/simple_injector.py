HUGE2 = """

huge_raw_input(argv[{0}]);
"""

import os, sys

filename = sys.argv[1]
huge2 = int( sys.argv[2] )
argv_num = sys.argv[3]

HUGE2 = HUGE2.replace("{0}", argv_num)

f = open(filename, "r")
contents = f.readlines()
f.close()

contents.insert(huge2, HUGE2)

f = open(filename, "w")
contents = "".join(contents)
f.write(contents)
f.close()
