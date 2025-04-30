#!/bin/bash

#  Generate 1 megabyte of random data
pv /dev/random | head -c 1M > testdata.bin

# Generate less random data by reusing hdd JSON
bzip2 --decompress --stdout < bigf.json.bz2 | head -c 4G| pv  > testdata-4G.bin