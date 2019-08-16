#!/bin/bash
mkdir factory

echo "Compile SpeedBump"
cd llvm_pass/bump
rm -rf build
mkdir build
cd build
cmake ..
make
cp skeleton/libSkeletonPass.so ../../../factory/libSkeletonPass_bump.so
cd ../../..


echo "Compile Anti-symbolic execution"
cd llvm_pass/anti
rm -rf build
mkdir build
cd build 
cmake ..
make
cp skeleton/libSkeletonPass.so ../../../factory/libSkeletonPass_antisym.so
cd ../../..

echo "Compile delay-primitives"
cd llvm_pass/bump/delaysrc
cp ../../../../lib/csmith/*.h .
clang -c *.c
rm -f *.h
cd ../../..

echo "Compile ROP-based trap's dummy file"
cd llvm_pass/trap
clang -c rop_dummy.c
rm -rf build
mkdir build
cd build
cmake ..
make
cp skeleton/libSkeletonPass.so ../../../factory/libSkeletonPass_rop.so
cd ../../..

echo "Compile pandora-pass file"
cd llvm_pass/pandora
rm -rf build
mkdir build
cd build
cmake ..
make
cp skeleton/libSkeletonPass.so ../../../factory/libSkeletonPass_coverage.so
cd ../../..

echo "compile huge.o"
cd llvm_pass/trap
clang -c huge.c
clang -c huge_dummy.c
clang -c delay_slp* > /dev/null 2> /dev/null
cd ../..

echo "compile anti-analysis library - anti-symbolic execution"
cd llvm_pass/anti
clang -c antilib.c
clang -c antilib_dummy.c
cd ../..

echo "Done"
