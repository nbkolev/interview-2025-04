
* Attempt to execute
``` commandline
~/$ chmod +x ./a
~/$ ./a
Segmentation fault.
```

* Install IDA Disssasembler perform step by step trace
* Try to create file ./pesho, then directory - nothing changes.
* Rename executable to `./pesho` as this string is suspiciously close to beginning of execution and got output:
```commandline
~/$ cp ./ ./pesho
~/$ ./pesho
0 127
1 69
2 76
3 70
4 2
5 1
6 1
...
```
* Output stays the same after multiple executions it seems to be produced by printf("%d %d/n") the "%d %d/n" string is visible in the disassembly.
* From the dissassembly data looks static, not computed.
* The first column is monotonically increasing so examining the output by plotting it to LibreOffice Calc looks like some graph:
![alt text](A-output-plot.png)
* As it resembles first derivative of acceleration - we will attempt integration:
* ![alt text](A-output-integrated-plot.png)
# Conclusion
Making and "informed assumption" this looks like an increasing trend of some sort could be number of clients of a company, increasing revenue, total data served or etc. 