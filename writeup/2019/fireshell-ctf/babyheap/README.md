# fireshell CTF (babyheap)
1337を入力することで利用できる隠しコマンドをデコンパイラなどを駆使して見つける  
隠しコマンド(Fill)はCreate+Editの動作  

各コマンドは1回しか利用できない。  
回数制限を管理しているフラグが0x6020a0以降にある  
```
0x6020a0: createのフラグ
0x6020a8: editのフラグ
0x6020b0: showのフラグ
0x6020b8: deleteのフラグ
0x6020c0: fillのフラグ
0x6020c8: p
```
引用:https://hackmd.io/@Xornet/Hketbw16L#:~:text=~~%20%E4%B8%AD%E7%95%A5%20~~%0A0x6020a0%3A%20create%E3%81%AE%E3%83%95%E3%83%A9%E3%82%B0%0A0x6020a8%3A%20edit%E3%81%AE%E3%83%95%E3%83%A9%E3%82%B0%0A0x6020b0%3A%20show%E3%81%AE%E3%83%95%E3%83%A9%E3%82%B0%0A0x6020b8%3A%20delete%E3%81%AE%E3%83%95%E3%83%A9%E3%82%B0%0A0x6020c0%3A%20fill%E3%81%AE%E3%83%95%E3%83%A9%E3%82%B0%0A0x6020c8%3A%20p

フラグを0で書き換える  
このときpをatoi@gotに変更しておく  

pがatoi@gotなのでeditでGOT Overwriteができる  
atoi@gotをsystemに書き換える  
atoiは入力を引数に取るのでメニューの際に  
```
------- BabyHeap -------
1 - Create
2 - Edit
3 - Show
4 - Delete
5 - Exit
> /bin/sh
```
という入力をすることで`/bin/sh`が引数と渡され、systemが実行される  

p.s.
手元の環境だと立ち上げたシェルで`ls`コマンドを利用すると`Segmentation fault (core dumped)`が返ってきて表示を受け取れなかった  
しかし、`cat solve.py`, `echo hoge`などは利用できたので多分大丈夫そう。  
