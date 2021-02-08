stack BOF

`__libc_csu_init`を使ってwriteを呼び出して、アドレスをリークする。  
rbxを0にすると好きな関数が呼び出せるようになる。  
`__libc_csu_init`を使うと引数が3つまでの好きな関数が呼べるみたい。  
`rbp == rbx+1`に調整するのに注意が必要。  

まず１回それでwriteのアドレスをリークする。  
https://libc.blukat.me/ でsymbolをwrite,addressに1d0をいれる。  
アドレスは下三桁で良い。  
アドレスの値からlibcのバージョンを特定してくれる。  

あとはそこからlibcをダウンロードするなりしてオフセットを計算してsystem("/bin/sh")して終了  

# 参考
http://inaz2.hatenablog.com/entry/2014/07/31/010158  
https://libc.blukat.me/

# Writeup Blog
https://kisqragi.hatenablog.com/entry/2021/02/08/131157
