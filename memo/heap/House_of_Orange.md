# House of Orange
解説ではなく、解くときに役立ちそうなこと。  

## 概要
topのサイズを改竄してfreeさせるやつ。  

## メモ
* topの改竄でfreeされる際チャンクの大きさは`改竄サイズ-0x20`
    * freeされる際topの末尾にfencepostが設置されるから
        * fencepostは0x10サイズのチャンクが2つ
    * それに伴いfreeできるサイズは0x40以上でないといけない  
        * fencepost分の0x20
        * チャンクの最小サイズは0x20
* freeされたチャンクはtcacheへいく
* topのアドレス+トップのサイズは常に0x1000でアライメントされていないといけないので注意する。  
* <b>topサイズの変更は現在のtopサイズの下3桁(16進数)を利用する。  </b>
    * malloc前に現在のtopのサイズを確認する。
    * そのサイズの下3桁を利用する。  

例：  
```
gdb-peda$ heapinfo
(0x20)     fastbin[0]: 0x0
(0x30)     fastbin[1]: 0x0
(0x40)     fastbin[2]: 0x0
(0x50)     fastbin[3]: 0x0
(0x60)     fastbin[4]: 0x0
(0x70)     fastbin[5]: 0x0
(0x80)     fastbin[6]: 0x0
(0x90)     fastbin[7]: 0x0
(0xa0)     fastbin[8]: 0x0
(0xb0)     fastbin[9]: 0x0
                  top: 0x560431af82b0 (size : 0x20d50) 
       last_remainder: 0x0 (size : 0x0) 
            unsortbin: 0x0
```
こうなっていたらtopのサイズは`0x20d50`なので改竄後の値は`0xd50`にする。  
すると常にtopアドレス+topサイズの結果が0x1000にアライメントされた状態になる。  
また実際に値を利用するときにはPREV_INUSEにビットが立っている必要があるので、`0xd51`を利用する。  