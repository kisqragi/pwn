# heap関連の知識メモ

callocはtcacheのチャンクを利用しない([参考](https://github.com/kisqragi/pwn/tree/main/writeup/2021/hsctf/house_of_sice))  

tcacheはfd同士でリンクしている  
fd -> fd -> ..
そのためfastbinから移動してきた時は値が0x10増えている

fastbinのチャンクのfdは次のチャンクの先頭を指している(次のチャンクのfdを指しているわけではない)