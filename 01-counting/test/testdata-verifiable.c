#include <stdio.h>
#include <stdint.h>

#define COUNT 1000000
uint32_t buffer[COUNT];

void main(void){

    // Produce 100 repeating numbers
    for (int i =0;i < COUNT; i++){
        uint32_t recurring_number = i % 100;
        buffer[i] = recurring_number;
    }

    buffer[10] = 100000; //Add unique number seen only once


    FILE *write_ptr = fopen("test.bin","wb"); ;
    fwrite(buffer,sizeof(buffer),COUNT,write_ptr);
    fclose(write_ptr);
}

// Expected results:
// 1 numbers seen only once
// 101 unique numbers