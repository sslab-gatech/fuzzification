# About Fuzzification

**Fuzzification** helps developers protect the released, binary-only software from attackers who are capable of applying state-of-the-art fuzzing techniques. Given a performance budget, this approach aims to hinder the fuzzing process from adversaries as much as possible.


# Existing Fuzzification components

* **SpeedBump**: Amplifies the slowdown in normal executions by hundreds of times to the fuzzed execution.
* **BranchTrap**: Interfers with feedback logic by hiding paths and polluting coverage maps.
* **AntiHybrid**: Hinders taint-analysis and symbolic execution.

# Envorinment

Tested on Ubuntu 16.04 64bit and LLVM 5.0 (with gold plugin)

# Quick start

* [Install instructions](docs/install.md)
* [Usage instructions](docs/usage.md) 

# Authors

* **Jinho Jung (Point of Contact)** <jinho.jung@gatech.edu>
* Hong Hu <hhu86@gatech.edu>
* David Solodukhin <david.solodukhin@gatech.edu>
* Daniel Pagan <dpagan@gatech.edu>
* Kyu Hyung Lee <kyuhlee@uga.edu>
* Taesoo Kim <taesoo@gatech.edu>

# Publications

```
@inproceedings{jung2019fuzzification,
  title={FUZZIFICATION: Anti-Fuzzing Techniques},
  author={Jung, Jinho and Hu, Hong and Solodukhin, David and Pagan, Daniel and Lee, Kyu Hyung and Kim, Taesoo},
  booktitle={28th USENIX Security Symposium (USENIX Security 19)},
  pages={1913--1930},
  year={2019}
}
```