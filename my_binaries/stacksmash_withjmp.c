// arm-linux-gnueabi-gcc stacksmash_withjmp.c  -fno-stack-protector -fno-stack-protector -z execstack -z norelro -no-pie -o vuln_stacksmach_withjump
#include <stdio.h>
#include <unistd.h>

int main()
{
  char buffer[0x20];
  read(0, buffer, 0x100);
  return 0;
}

void jmp(){
  __asm__("blx %sp");
  return;
}


