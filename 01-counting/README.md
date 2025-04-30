# Description
* Data is read by 1 MB chunks. 
* For every chunk data is converted with `numpy.frombuffer(chunk, dtype=numpy.uint32)` and processed with `numpy.unique_counts()`
* Frequencies in the chunk are binned by `bin_id = value % BIN_COUNT` and bins are aggregated as files in `./frequencies/{bin_id}.pickle`.
* As a result python process consumes no more than 20 MB of RAM when processing test non white noise data.
* A generator `get_binned_frequencies()` yields the bins to the aggregating functions for the required subtasks a) "count the unique numbers" and b) "count the unique numbers"

# Consideration
* The optimal solution to this task is heavily dependent of the frequency distribution of the uint32 integers in the input file.
* As **the company specializes in data storage the implementation is tailored to processing large files** with efficient memory use.
Otherwise, it would be pointless to bother with chunked processing and the main processing could be reduced to:
```
import numpy as np

frequencies = np.unique_counts(np.fromfile(sys.stdin, dtype=np.uint32))
```

# Development notes

* During development an example non white noise file was produced by reusing the hdd data provided `bzip2 --decompress --stdout < bigf.json.bz2 | head -c 4G  > testdata-4G.bin`
* The processing.py executable supports --stdin and --file switches
* In order to test whether counting is indeed correct a synthetic test file was provided by `testdata-verifiable.c`

# Requirements
* Python + numpy (any recent versions)
* pv, bzip2
