# simultaneity
## 実行
ldが配られているのでpatchelfでデバッグが楽になるよ。  
```sh
# patchelf --set-rpath simultaneity/ --set-interpreter simultaneity/ld-linux-x86-64.so.2 simultaneity
```

## メモ
大きなチャンクを確保するとlibc leakできる。(offsetが同じになるので）  
mallocで返された値 <-----> libc baseのアドレス  
このオフセットが同じになる  
色々して__free_hookをone_gadegetに置き換える。  
one_gadegetの発火はscanfで大きな数字列を入力する。  
具体的には`00000000000000000000000012345`のような形で先頭に0を大量につける。  
先頭に0を足しても値は変わらないが、入力文字列が長くなると内部でfreeが走るためone_gadegetが発火する。  
理由は詳しくは読んでいないためわからないが、バッファを一度freeして再度新しいバッファ領域を確保するためではないかと推測している。  
