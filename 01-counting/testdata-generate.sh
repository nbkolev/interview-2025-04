#!/bin/bash

#  Generate 1 megabyte of random data
pv /dev/random | head -c 1M > testdata.bin