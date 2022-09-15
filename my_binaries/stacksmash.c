#include <stdio.h>
#include <unistd.h>

int main(){
    char buffer[0x20];
    read(0,buffer,0x100);
    return 0;
}
