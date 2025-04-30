#!/bin/bash
pv bigf.json.bz2 | bzip2 --decompress --stdout | python processing.py --stdin