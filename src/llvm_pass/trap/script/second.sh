#!/bin/bash

$CC -W -Wall -Wstrict-prototypes -Wmissing-prototypes -Wshadow -flto -std=gnu99 -flto -fuse-ld=gold  -o readelf readelf2.o version.o unwind-ia64.o dwarf.o elfcomm.o dummy.o ../libiberty/libiberty.a -lz -ldl

cp ./readelf /data/sslab/anti-fuzz/src/defense/
