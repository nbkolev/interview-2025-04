* Attempt to execute
```commandline
~/$ chmod +x ./b
~/$ ./b
Segmentation fault.
```

* After some fidding with the dissasembler the SIGSEGV is located after "TMPDIR" string which immediately strikes as environment variable. Some progress is apparent:
```commandline
~/$ chmod +x ./b
~/$ TMPDIR=./ ./b 
Init done 0 .
Enter password: 

```
Trying any text outputs "WRONG" (nothing less expected:) )
* Continuing to fiddle with the interactive debugger a strange looking sequence of printable characters in pointed from the stack after sys_read() call :
```commandline
momdkvjhradj|l|`|ps~u{w~vjnrr|?
```

* after trying psudo C code disassembly the following segment is apparent:
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
* it looks like sys_read() is in v11[] and v10[] contains the strange characters "momdkvjhradj|l|`|ps~u{w~vjnrr|?" which are probably obfuscated by some sort of XOR operation. 
* We need to try to simulate it in plain C as XOR operation is reversible:

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

```commandline
~/$gcc reverse-xor.c -o reverse-xor
~~/$ ./reverse-xor 
mnogoslozhnaparolaamanainstina
```
# Final result
```commandline
~/$ TMPDIR=./ ./b 
Init done 0 .
Enter password: mnogoslozhnaparolaamanainstina

OK.

```