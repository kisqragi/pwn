# heap関連の知識メモ

callocはtcacheのチャンクを利用しない([参考](https://github.com/kisqragi/pwn/tree/main/writeup/2021/hsctf/house_of_sice))  

tcacheはfd同士でリンクしている  
fd -> fd -> ..
そのためfastbinから移動してきた時は値が0x10増えている

fastbinのチャンクのfdは次のチャンクの先頭を指している(次のチャンクのfdを指しているわけではない)

<<<<<<< HEAD
# リンクの順序
## LIFO
* tcache
* fastbin
## FIFO
* unsorted bin
=======
## 一番最初に確保されるチャンク
parseheapすると自分が確保したチャンクより前に何かしらのチャンクが確保されているのが確認できる。  
`libc-2.27.so`だと`0x250`, `libc-2.31.so`だと`0x290`のようだが、まだ確認はしていない。  
下の例では自分で確保した0x20のチャンクより前に0x250のチャンクが確保されている。  
```
gdb-peda$ parseheap
addr                prev                size                 status              fd                bk                
0x5614c75db000      0x0                 0x250                Used                None              None
0x5614c75db250      0x0                 0x20                 Used                None              None
```
参考:https://hackmd.io/@Xornet/Sk9_mV7CL#tcache_perthread_struct
>>>>>>> 967d631c58d15ee9fc4b681d2fd763b9eb69e377
