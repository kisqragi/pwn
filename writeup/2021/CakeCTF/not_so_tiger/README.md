std::variant型は末尾１バイトでどの型を利用しているか決めている。  
gdbでcatを表示するとindexという表記がされている。  
bofで型を書き換えて、任意アドレスの読み込みを行う。  

libc.environを表示するとreturn addressが積まれているアドレスが表示される。  
そこからスタックアドレス→canaryと表示してROPする。  
