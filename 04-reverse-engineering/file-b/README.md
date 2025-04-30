## 1. Attempt to execute
```commandline
~/$ chmod +x ./b
~/$ ./b
Segmentation fault.
```
## 2. Inspect with disassembler
* After some fidding we find that **SIGSEGV is located after "TMPDIR" string** which immediately strikes as an attempt to read a missing environment variable. Some progress is apparent:
```commandline
~/$ chmod +x ./b
~/$ TMPDIR=./ ./b 
Init done 0 .
Enter password: 

```

* Trying some random text as "password" results im  "WRONG" output. (behaviour seems expected).
* Continue with more disassembler step by step trace an we approach **a suspicious sequence of printable characters** present soon after the sys_read() call in the stack:
```commandline
momdkvjhradj|l|`|ps~u{w~vjnrr|?
```

## 3. Try disassembly to pseudo C code
* The following segment is of interest as "WRONG" stdout is directly dependent on it:
```code
 for ( i = 0; i <= 29; ++i )
  {
    if ( (i ^ (char)v11[i]) != v10[i] )
    {
      sub_4082F0("WRONG");
      sub_406E80(4);
    }
  }
  sub_4082F0("OK.");
  return 0;
```
* It looks like sys_read() is in v11[] and v10[] contains the strange characters `momdkvjhradj|l|`|ps~u{w~vjnrr|?` which are **probably obfuscated by some sort of XOR** operation. 
## 4. XOR operation is reversible. 
Try to perform the reverse in **plain C**:

```c
#include <stdio.h>

char v10[] = "momdkvjhradj|l|`|ps~u{w~vjnrr|?";
char result[100];

void main(void){
    for (int i = 0; i <= 29; ++i )
    {
        result[i] = (i ^ (char)v10[i]);
    }
    printf("%s", result);
}

```
* Compile and run
```commandline
~/$gcc reverse-xor.c -o reverse-xor
~~/$ ./reverse-xor 
mnogoslozhnaparolaamanainstina
```
## 5. Final result
```commandline
~/$ TMPDIR=./ ./b 
Init done 0 .
Enter password: mnogoslozhnaparolaamanainstina

OK.

```
