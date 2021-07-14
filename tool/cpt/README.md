# CPT
CPT is a tool to create pwn solver templates.  

## Runnig CPT
```sh
$ cpt
```
When the above command is executed, the following template will be created.  
```python
from pwn import *
elf = ELF('chall', checksec=False)
context.binary = elf

if args.REMOTE:
    s = remote('localhost', 10000)
    libc = ELF('libc.so.6', checksec=False)
else:
    s = process('chall')
    libc = ELF('/lib/x86_64-linux-gnu/libc.so.6', checksec=False)

s.interactive()
```

You can change the output by setting arguments and options.  
```sh
$ cpt example.com 9999 --checksec
```
```python
from pwn import *
elf = ELF('chall', checksec=True)
context.binary = elf

if args.REMOTE:
    s = remote('example.com', 9999)
    libc = ELF('libc.so.6', checksec=True)
else:
    s = process('chall')
    libc = ELF('/lib/x86_64-linux-gnu/libc.so.6', checksec=True)

s.interactive()
```
