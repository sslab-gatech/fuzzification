#!/bin/bash
cp /data/fuzz/sample/binutils-2.25/binutils/readelf.o .
opt -always-inline -load skeleton/libSkeletonPass.so -SkeletonPass <readelf.o> readelf2.o
cp ./readelf2.o /data/fuzz/sample/binutils-2.25/binutils/readelf2.o
cp ./dummy.o /data/fuzz/sample/binutils-2.25/binutils/dummy.o
