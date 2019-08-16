#!/bin/bash
opt -always-inline -load ./libSkeletonPass_rop.so -SkeletonPass <$1.o2> $1_coverage.o
