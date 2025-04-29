# Requiirements

* Python (any recent version)
* bzip2, pv
* bigf.json.bz2 present in analysis.sh directory

# Description
As the provided file is degenerate JSON case in order to parse it with reasonable time and memory constraints it is not processed using built-in JSON in Python 

* To save memory the file is processed in 1MB chunks. As a result python process consumes no more than 20 MB of ram.
* Each object in the chunks is parsed with compiled regex.
* File is decompressed on the fly and piped to the Python executable.

# Development notes

* During development a smaller input file was produced with `bzip2 --decompress --stdout < bigf.json.bz2 | head -c 2M  > test.txt`
* The processing.py executable supports --stdin and --file switches.

# Result of execution:

Runtime is around 20 minutes on Intel Core i3-12100/DDR4 3000Mhz running Ubuntu 6.14.0-15-generic on VirtualBox:

```console
2,69GiB 0:19:07 [2,40MiB/s] [================================================>] 100%            
Records processed: 400000000
Aggregating results...
HDD models present: 13
Models found sorted in ascending order:
MODEL: 1
123456789: 33327094
SSDDC1: 33327742
SSDF1: 33328579
broken: 33328584
SCSI3HD: 33329611
HGST2048T: 33332531
RDV2: 33332954
DSD07461: 33333959
HGST3T: 33337292
HGST8T: 33337967
DRV1: 33338513
SSDLP2: 33345174
Done.
```


