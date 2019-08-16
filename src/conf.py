import os
import sys

# working directory
COMPILE_ROOT = "../antifuzz-tutorial/temp"
#COMP_DIR = os.path.join(COMPILE_ROOT, "binutils")

# sample directory
TMP_DIR = "/tmp"
EVAL_REPO = "../antifuzz-tutorial"
EVAL_REPO_TEST = "samples"
EVAL_REPO_SAMPLE = "binaries"
EVAL_REPO_PATCH = "patches"
INFO_DIR = os.path.join(TMP_DIR, "antifuzz")


##### customize target
SAMPLE = "readelf"
ARGS = " -a "
COMP_DIR = os.path.join(COMPILE_ROOT, "binutils")

#SAMPLE = "objdump"
#ARGS = " -d "
#COMP_DIR = os.path.join(COMPILE_ROOT, "binutils")

#SAMPLE = "nm-new"
#ARGS = " "
#COMP_DIR = os.path.join(COMPILE_ROOT, "binutils")

#SAMPLE = "objcopy"
#ARGS = " -S "
#COMP_DIR = os.path.join(COMPILE_ROOT, "binutils")

MID_ARGS = False
DEFAULT_ARG = " test"
if MID_ARGS == True:
	ARGS = " "

##### customize fuzzer
MOD_AFL = "../fuzzer/afl-2.51b-bbcheck"
SHOWMAP = os.path.join(MOD_AFL, "afl-showmap")
AFL_FUZ = os.path.join(MOD_AFL, "afl-fuzz")

##### setup working directory
CSMITH_DIR = "../lib/csmith"
CORRECT_FUZ_INPUT = "cor_fuzz"

SAMPLE_DIR = os.path.join(EVAL_REPO, "test", EVAL_REPO_SAMPLE)
PATCH_DIR = os.path.join(EVAL_REPO, "test", EVAL_REPO_PATCH)
CORRECT_INPUT = os.path.join(EVAL_REPO, "test", EVAL_REPO_TEST, SAMPLE, "cor")
INCORRECT_INPUT = os.path.join(EVAL_REPO, "test", EVAL_REPO_TEST, SAMPLE, "incor")
OUTPUT_DIR = os.path.join(EVAL_REPO, "test", "output")
CORRECT_BB_DIR = os.path.join(INFO_DIR, "corbb")
INCORRECT_BB_DIR = os.path.join(INFO_DIR, "incorbb")

BB_NAME = "BB_count"
BB_EXTENTION = ".bb"
INST_TARGET = "INST_BB"
TOTAL_BB = "/tmp/makeout"
TOTAL_BB_DIR = TOTAL_BB

DELAYPASS = "bump"
DELAY_COLLISION = os.path.join(".", "llvm_pass", "trap")
DELAY_USLP = os.path.join(".", "llvm_pass", "bump", "delaysrc")
DEFENSE = os.path.join(".", "llvm_pass", "trap")
SCRIPTPASS = "factory"
WORKING_DIR = "./.work3"
TARGET_FILES = "/tmp/target_files"

FUZZ_INPUT_DIR = "/tmp/fuzzinput"
FUZZ_OUTPUT_DIR = "/tmp/fuzzoutput"
TOTAL_FUZZ_TIMEOUT = 120 # seconds
FUZZ_TIMEOUT = "2000" #ms

# relative reference
COMPILER = " ../fuzzer/afl-2.51b-bbcheck/afl-clang-fast"
COMPILE_ROOT = "../antifuzz-tutorial/temp"
DELAYOBJ = "huge.o" # default name
