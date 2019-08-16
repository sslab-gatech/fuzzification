
#!/bin/bash
cd skeleton
make clean
make
cd ..
cp skeleton/libSkeletonPass.so ./toytest/
cd  toytest
make clean
make
cd ..
cp toytest/toy .
cp toytest/dummy.o .
