#include <stdio.h>
#include <unistd.h>

void shell(){
    system("/bin/sh\x00");
    return 0;
}

int main(){
    char buffer[0x20];
    read(0,buffer,0x100);
    return 0;
}
