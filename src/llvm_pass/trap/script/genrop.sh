#!/bin/bash
ROPgadget  --only "pop|ret" --nojop --nosys --all --binary $1 |grep " : " |grep -v "ret\ "  > ropgadget_temp
#ROPgadget --depth=2 --only "ret" --all --binary $1 |grep " : " |grep -v "ret\ "  > ropgadget
