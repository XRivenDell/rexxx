#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

void shell(){
    system("/bin/sh\x00");
}

int main(){
    char buffer[0x20];
    read(0,buffer,0x100);
    return 0;
}
