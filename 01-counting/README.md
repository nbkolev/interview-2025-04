# Data entropy
Examining the file size difference between compressed and decompressed file gives us the hint that the contents are not evenly distributed as the file would be incompressible (see Shannon theorem).

# Additional consideration
As the company specializes in data storage the implementation is tailored to processing large files with efficient memory use.
Otherwise, it is pointless to bother with chunked processing and all input could be parsed like this:
```
import numpy as np

integer_array = np.fromfile(sys.stdin, dtype=np.uint32)
```

# Requirements
* Python + numpy (any recent versions)
* pv, bzip2

# Description
