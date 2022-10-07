// arm-linux-gnueabi-gcc stacksmash_withshell.c -fno-stack-protector -fno-stack-protector -z norelro -no-pie -o vuln_stacksmash_withshell
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
