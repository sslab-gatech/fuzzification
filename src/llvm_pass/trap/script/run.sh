#!/bin/bash

(cd /data/fuzz/sample/binutils-2.25/binutils;sh ./first.sh)
sh ./readelf.sh
(cd /data/fuzz/sample/binutils-2.25/binutils;sh ./second.sh)
