# https://github.com/sslab-gatech/fuzzification/blob/master/docs/install.md
FROM ubuntu:16.04
WORKDIR /home

# Install dependencies
RUN apt -y update
RUN apt -y upgrade
RUN apt -y install git python python-pip python-dev cmake libffi-dev wget ocaml libssl-dev build-essential

# (1) Install clang and llvm
##### Download llvm & clang source code
RUN wget http://llvm.org/releases/5.0.0/llvm-5.0.0.src.tar.xz
RUN wget http://llvm.org/releases/5.0.0/cfe-5.0.0.src.tar.xz
RUN git clone --depth 1 git://sourceware.org/git/binutils-gdb.git binutils
##### Extract source
RUN tar xvf llvm-5.0.0.src.tar.xz
##### Extract clang src into the llvm tools directory
RUN tar xvf cfe-5.0.0.src.tar.xz --directory llvm-5.0.0.src/tools
##### Clean up
RUN rm llvm-5.0.0.src.tar.xz cfe-5.0.0.src.tar.xz
# Compile llvm with DLLVM_USE_LINKER and DLLVM_BINUTILS_INCDIR
RUN cd llvm-5.0.0.src &&                             \
    mkdir build &&                                   \
    cd build &&                                      \
    CC=gcc CXX=g++ cmake -DCMAKE_INSTALL_PREFIX=/usr \
    -DLLVM_ENABLE_FFI=ON                             \
    -DCMAKE_BUILD_TYPE=Release                       \
    -DLLVM_BUILD_LLVM_DYLIB=ON                       \
    -DLLVM_USE_LINKER=gold                           \
    -DLLVM_BINUTILS_INCDIR=/home/binutils/include    \
    -DLLVM_TARGETS_TO_BUILD="host;AMDGPU"            \
    -Wno-dev ..
RUN cd llvm-5.0.0.src/build && make -j4
RUN cd llvm-5.0.0.src/build && make install

# (2) Compile LLVM-Pass
RUN git clone --recurse-submodules https://github.com/sslab-gatech/fuzzification.git
RUN cd fuzzification/src && ./compile_pass.sh

# (3) Install modified AFL
ENV AFL_I_DONT_CARE_ABOUT_MISSING_CRASHES=1
ENV AFL_SKIP_CPUFREQ=1
##### Install dependencies
RUN apt -y install libtool-bin automake bison libglib2.0-dev
##### Compile the provided AFL-2.51b (namely, bbcheck)
RUN cd fuzzification/fuzzer/afl-2.51b-bbcheck && make
RUN cd fuzzification/fuzzer/afl-2.51b-bbcheck/llvm_mode && make
RUN cd fuzzification/fuzzer/afl-2.51b-bbcheck/qemu_mode && ./build_qemu_support.sh || echo "TODO: Fix: Error: afl-qemu-trace instrumentation doesn't seem to work!"
##### Create a link to the binary
RUN ln fuzzification/fuzzer/afl-2.51b-bbcheck/afl-clang-fast /usr/local/bin/afl-clang-fast

# (4) Install python requirements for fuzzification
COPY requirements.txt .
RUN pip install -r requirements.txt
