
Welcome to the Fuzzification. We will guide users about how to apply the technique on target application. Since we are working on LLVM-IR level instrumentation, we don't provide fully automated approach. Instead, user should understand compilation process of target application. This tutorial will introduce how to prepare prerequisites and how to apply Fuzzification on existing project. 

# Example application

We use [binutils](https://www.gnu.org/software/binutils/) for our example, especially [v2.23](https://ftp.gnu.org/gnu/binutils/binutils-2.23.tar.gz) which contains lots of bugs and reveals many crashes during the fuzzing. 

## Generate delay primitives

* `src/randomcode.py` will generate delay primitives for SpeedBump component. (another components for LLVM-IR instrumentation and BranchTrap/AntiHybrid should be compiled at this stage. If user don't finish this, please visit [Installation](install.md) first)
* There are several options for the generation. Important parameters are:
  * `DELAYS`: array for length of delay. If it is set as `[1,2,3]`, we will try to generate random code which will delay 1, 2, and 3 ms. 
  * `OFFSET`: allowable error on the length of delay. If use `0.2`, we will allow 20% of error.
* To generate delays, just run the script.
```bash
$ cd {repo}/src
$ python randomcode.py
```
* Upon completion, it will generate multiple codes for delay. For example, we will be able to see the three files, according to the configuration (`DELAYS = [1,2,3]`).
  * We recommend the user to generate various delays.
  * e.g., `[10,20,30,40,50,60,70,80,90, 100, 200, 300, 400, 500]`
```bash
$ {repo}/src/.csmith/delay_1.c
$ {repo}/src/.csmith/delay_2.c
$ {repo}/src/.csmith/delay_3.c
```
* Finally, user should check the generated delays to `{repo}/src/llvm_pass/bump/delaysrc` directory where Fuzzification actually refers and compile the file again using the script. 
(Don't forget to compile the generated code)

```bash
$ cd {repo}/src
$ ./compile_pass.sh
```

## Compile binutils using clang (modified afl-clang-fast)

* Actually, Fuzzification is made for the developer who knows about the source code and has many samples (or test-cases) for testing. Therefore, Fuzzification requires some (very few) knowledge about the code. 
* In this tutorial, we will introduce where to modify in the code for the Fuzzification. Before that, let's compile the target binaries (readelf, nm-new, objdump, and objdump) using script that we provided. 
```bash
$ cd {repo}/antifuzz-tutorial
$ python compile.py

```
* Important directories 
```bash
antifuzz-tutorial/archive # store original source code
antifuzz-tutorial/temp    # temporary directory for the compilation
antifuzz-tutorial/test/binaries # has copy of original binary for overhead measurement
antifuzz-tutorial/test/patches  # contain code patch information (e.g., where to inject)
antifuzz-tutorial/test/samples  # contain correct/incorrect sample for target
antifuzz-tutorial/test/output   # store fuzzified binary here
```
  * Most importantly, user can check the generated output from `antifuzz-tutorial/test/output` directory. 

## Apply fuzzification

* Fuzzification configuration: user can adjust options. Plesae read our [paper](https://www.usenix.org/system/files/sec19fall_jung_prepub.pdf) about the detail of these options. 

* `antifuzz_all.py`
```python
DELAYS         = [30,50,70,100,200,300] # try these delays (ms) to the binary and find best one
OVERHEAD       = [3]  # user can check different overhead budget
NON_VISIT_BUMP = 5 # ratio of non-visited-BBs for SpeedBump
NON_VISIT_COV  = 5 # ratio of non-visited-BBs for BranchTrap
NON_VISIT_ANTI = 5 # ratio of non-visited-BBs for AntiHybrid

NORMAL_COV     = 1 # ratio of non-visited-BBs for BranchTrap (for all fuzzifications)
NORMAL_ANTI    = 5 # ratio of non-visited-BBs for AntiHybrid (for all fuzzifications)

INCLUDE_NON_VISIT = True # should we include non-visited-BBs for the instrumentation?
PROCESS_INCORRECT = True # should we instrument error-handling routine?
```
* `conf.py`
```python
SAMPLE = "readelf"  # fuzzifying binary name
ARGS = " -a "       # argument for measuring overhead
COMP_DIR = os.path.join(COMPILE_ROOT, "binutils") # compilation path
```

* After choose one desirable setup, user can run the script for the fuzzificaction.
```bash
cd {repo}/src
python antifuzz_all.py
```
  * You can check the fortified binary under `{repo}/antifuzz-tutorial/test/output`
  * If user generated all `readelf` binaries without any problem, user will be able to see `readelf_ori`, `readelf_all`, `readelf_bump`, `readelf_coverage`, and `readelf_anti` under this directory.

---

# How to apply Fuzzification on arbitrary project?

Ok, now you see how the fuzzification generate target binary. You may notice that user of fuzzification should tell where to modify at the source code. However, we hope you do not worry about that too much. Our example will help the user understand necessary code modifications. 

Let's use another binary from the binutils project. This time we will provide detail instruction for fortifying `objdump` binary. 

The overall process is as follows:

1. Patch the original code (usually the file with `main()` function)
2. Put samples (correct, incorrect) and patched code into working directory
3. Run normal compilation and store the compilation commands
4. Provide the part of compilation command to Fuzzification framework with notation
5. Provide the actual command for executing target binary

## Patch the original code

We need to modify the code to define global variables and to guide Fuzzification about where to patch. To help the patch, we provide three code injector and they are under `{repo}/src/code_injector/`

* There are three code injectors
  * simple_injector: inject one function to wrap the argument of filename (i.e., input file's path)
  * jtable_injector: inject global variables for storing jump-table of ROP-based BranchTrap
  * anti-taint: transform explicit data-flow into implicit data-flow 

* simple_injector.py
  * arg#1: target source code filename
  * arg#2: line to inject the wrapper
    * we recommend the line number as begining of the main function
  * arg#3: position of input file 
    * we assume `objdump -d inpurfile` as fuzzing command. In this case, inputfile name is at the second argument of the command; thus user can use `2` for this argument. 
  * So user can inject the code by using the following command.
```bash
$ python simple_injector.py objdump.c 3418 2
```

* jtable_injector.py
  * arg#1: target source code filename
  * arg#2: line to inject the reference to jump-table
    * we also recommend this line number be the beginning of the main function. So user can just use the same line number as above.
```bash
$ python jtable_inject.py objdump.c 3418
```

* anti-taint.py
  * arg#1: target source code filename
  * arg#2: modified code's filename 
  * arg#3: ratio of data-flow transformation
  * **NOTE** that the injection should be on top of the abobe two commands and user should separately store the result by adding `_anti` postfix. 
```bash
python anti-taint.py objdump.c objdump_anti.c 30
```

## Put files under working directory

We can keep use `{repo}/antifuzz-tutorial` as our working directory, if you want to change the working directory, you can change `EVAL_REPO` from `{repo}/src/conf.py` file. User should put currect files under this directory, specipically under `{repo}/antifuzz-tutorial/test`. 


* **samples** directory: user should provide correct and incorrect samples to fuzzification. Since we are forifying `objdump`, user should create directory `objdump/cor` and `objdump/incor` under samples directory, then put samples for the profiling. 
  * We already put samples for `objdump` to the directory. Please check the directory if you want to make sure about the correect setup. 

* **patches** directory: user should provide patched source code. We will introduce how to patch the code at the next section. Necessary files are:
  * `objdump.c`: changed to contain necessary global variables as well as input-sensitive functions. We use this code for all compilation. If user choose not to use specific component, we will replace the called function with dummy function. 
  * `objdump_anti.c`: changed to some character arrays to pass implicit data-flow to hinder dynamic taint analysis.
  * We also placed the necessary files under the correct directory, please check the directory. 

## Collect original compilation commands

User should extract original compilation script from the project. For the binutils package,

```bash
./configure --disable-werror --disable-silent-rules
make > output
```

will store the actual commands used for the compilation. Among many commands, we only need two commands to generate `objdump` binary and `objdump.o` file. User can easily identify these commands by searching for `-o objdump` and `-o objdump.o` strings.

```bash
# command for objdump.o
'afl-clang-fast -DHAVE_CONFIG_H -I.  -I. -I. -I../bfd -I./../bfd -I./../include -DLOCALEDIR="\\"/usr/local/share/locale\\"" -Dbin_dummy_emulation=bin_vanilla_emulation  -W -Wall -Wstrict-prototypes -Wmissing-prototypes -Wshadow -O0 -flto -std=c11 -lpthread -MT objdump.o -MD -MP -MF .deps/objdump.Tpo -c -o objdump.o -DOBJDUMP_PRIVATE_VECTORS="" ./objdump.c'

# command for objdump
"/bin/bash ./libtool --tag=CC   --mode=link afl-clang-fast -W -Wall -Wstrict-prototypes -Wmissing-prototypes -Wshadow -O0 -flto -std=c11 -lpthread  -flto  -o objdump objdump.o dwarf.o prdbg.o rddbg.o debug.o stabs.o ieee.o rdcoff.o bucomm.o version.o filemode.o elfcomm.o ../opcodes/libopcodes.la ../bfd/libbfd.la ../libiberty/libiberty.a  -lz"
```

## Provide compilation script to the configuration 

Now user can slightly modify the above command. Let's see the output first. The output is under `{repo}/antifuzz-tutorial/build_template.py`

```bash
# command for objdump.o
COMMAND["objdump.o"] = 'afl-clang-fast -DHAVE_CONFIG_H -I.  -I. -I. -I../bfd -I./../bfd -I./../include -DLOCALEDIR="\\"/usr/local/share/locale\\"" -Dbin_dummy_emulation=bin_vanilla_emulation  -W -Wall -Wstrict-prototypes -Wmissing-prototypes -Wshadow -O0 -flto -std=c11 -lpthread -MT objdump.o -MD -MP -MF .deps/objdump.Tpo -c -o objdump.o -DOBJDUMP_PRIVATE_VECTORS="" ./{SRC}  1> /dev/null 2> /tmp/makeout'

# command for objdump
COMMAND["objdump"] = "/bin/bash ./libtool --tag=CC   --mode=link afl-clang-fast -W -Wall -Wstrict-prototypes -Wmissing-prototypes -Wshadow -O0 -flto -std=c11 -lpthread  -flto  -o $1 {object} [[objdump.o dwarf.o prdbg.o rddbg.o debug.o stabs.o ieee.o rdcoff.o bucomm.o version.o filemode.o elfcomm.o]]  ../opcodes/libopcodes.la ../bfd/libbfd.la ../libiberty/libiberty.a  -lz 1> /dev/null 2> /dev/null"
```

Can you see the notations we applied? (and that you need to do for another Fuzzification) 

* **objdump.o**
  * actual source code filename `objdump.c`is changed to `{SRC}`

* **objdump**
  * actual output name `objdump` is changed to `{$1}`
  * list of object files are wrapped with `[[` and `]]`
  * `{object}` keyword is inserted in front of `[[`

## Provide execution command

Finally, user should tell which command to use for target binary execution. In this example, we assume that user will use `objdump -d filename`. 

To tell this, user should modify `conf.py` (under `{repo}/src/conf.py`).

```python
SAMPLE = "objdump"
ARGS = " -d "
```

That's all procedures that the user should prepare for applying Fuzzification. After all preparation, we can run the fuzzification script and check the output.

```bash
# Fuzzification
$ cd {repo}/src
$ python antifuzz_all.py

# Check the output
$ cd {repo}/antifuzz-tutorial/test/output
```
