# Envorinment

Tested on Ubuntu 16.04 64bit and LLVM 5.0 (with gold plugin)

# Installation Prerequisite

Before using Fuzzification, user should prepare llvm, clang, and proper (i.e., modified version) AFL fuzzer.  

## LLVM (with gold plugin)

* User can use llvm and clang with gold plug in. User can install through the below commands. 

```bash

# Install dependencies
$ sudo apt-get update
$ sudo apt-get install git python python-pip python-dev cmake libffi-dev

# Download llvm & clang source code
$ wget http://llvm.org/releases/5.0.0/llvm-5.0.0.src.tar.xz
$ wget http://llvm.org/releases/5.0.0/cfe-5.0.0.src.tar.xz
$ git clone --depth 1 git://sourceware.org/git/binutils-gdb.git binutils

# Extract source
$ tar xvf llvm-5.0.0.src.tar.xz
$ tar xvf cfe-5.0.0.src.tar.xz

# Copy clang src into the llvm tools directory
$ cd llvm-5.0.0.src
$ cd tools
$ mv ../../cfe-5.0.0.src .
$ cd ..

# compile the llvm with DLLVM_USE_LINKER and DLLVM_BINUTILS_INCDIR
# (NOTE: SHOULD specify correct binutils directory
# , i.e., replace YOUR_BINUTILS with user's path)
$ mkdir build && cd build
$ CC=gcc CXX=g++                              \
  cmake -DCMAKE_INSTALL_PREFIX=/usr           \
        -DLLVM_ENABLE_FFI=ON                  \
        -DCMAKE_BUILD_TYPE=Release            \
        -DLLVM_BUILD_LLVM_DYLIB=ON            \
        -DLLVM_USE_LINKER=gold                \
        -DLLVM_BINUTILS_INCDIR={YOUR_BINUTILS/include} \
        -DLLVM_TARGETS_TO_BUILD="host;AMDGPU" \
        -Wno-dev ..                          
$ make -j 4
$ make install
```

## Clone repository
```bash
$ git clone --recurse-submodules https://github.com/sslab-gatech/fuzzification.git
```

## LLVM-pass and necessary code objects

* Then, we need to compile `.so` files for IR-level instrumentation. This script will compile necessary `.so` files (SpeedBump, BranchTrap, AntiHybrid) as well as necessary object files (e.g., delay primitives).

```bash
$ cd {repo}/src
$ ./compile_pass.sh
```

## AFL (modified version that we provide)

* Fuzzification uses AFL fuzzer's functionality to measure the number of executed basic blocks so we modified the source code of AFL. The modified fuzzer is under `fuzzer/afl-2.51b-bbcheck`. 

* So user SHOULD use the provided fuzzers for generating **fuzzified** binary.

```bash
# Install dependencies
$ sudo apt-get install libtool-bin automake bison libglib2.0-dev

# Compile provided AFL-2.51b (namely, bbcheck)
$ cd {REPO}/fuzzer/afl-2.51b-bbcheck
$ make

$ cd llvm_mode
$ make
$ cd ..

$ cd qemu_mode
$ ./build_qemu_support.sh
$ cd ..

# Make link to the binary
$ sudo ln afl-clang-fast /usr/local/bin/afl-clang-fast

# Example command for compiling target application
$ export AFL_PATH={REPO}/fuzzer/afl-2.51b-bbcheck
$ export CC=afl-clang-fast
$ export CXX=afl-clang-fast
$ export RANLIB=llvm-ranlib
$ export CFLAGS=" -flto -std=gnu99 "
$ export LDFLAGS=" -flto -fuse-ld=gold "
$ ./configure
$ make
```

## Dependencies in source

```bash
$ sudo apt-get install python2.7 python-pip python-dev git libssl-dev libffi-dev build-essential
$ pip install executor
$ pip install tqdm
$ pip install --upgrade pwntools
```