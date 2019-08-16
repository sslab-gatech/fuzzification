#!/bin/bash
opt -load ./libSkeletonPass_coverage.so -SkeletonPass <$1_bump.o> $1.o2 
cp bb_cov INST_BB
opt -always-inline -load ./libSkeletonPass_rop.so -SkeletonPass <$1.o2> $1.o3
cp bb_anti INST_BB
opt -load ./libSkeletonPass_antisym.so -symb <$1.o3> $1_all.o 


