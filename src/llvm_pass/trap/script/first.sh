#!/bin/bash
$CC -DHAVE_CONFIG_H -I.  -I. -I. -I../bfd -I./../bfd -I./../include -DLOCALEDIR="\"/usr/local/share/locale\"" -Dbin_dummy_emulation=bin_vanilla_emulation  -W -Wall -Wstrict-prototypes -Wmissing-prototypes -Wshadow -flto -std=gnu99  -MT readelf.o -MD -MP -MF .deps/readelf.Tpo -c -o readelf.o readelf.c

$CC -W -Wall -Wstrict-prototypes -Wmissing-prototypes -Wshadow -flto -std=gnu99 -flto -fuse-ld=gold -o readelf readelf.o version.o unwind-ia64.o dwarf.o elfcomm.o ../libiberty/libiberty.a -lz -ldl
