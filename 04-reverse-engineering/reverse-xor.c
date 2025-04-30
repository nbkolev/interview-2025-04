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