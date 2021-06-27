# メモ
mallocの回数が16回という制限があるためfastbinを利用したDouble Freeが行えないというのがポイント。  
そこをcallocを使ってうまく回避していく。  

<b>callocはtcacheからチャンクを持ってこない</b>  

そのため、tcacheにチャンクがあっても、fastbinを利用することができる。    

## 大まかな流れ
1. 37,38,34,44行目の処理でtcacheを埋める
2. 40,41,46,47,48でfastbinにチャンクを格納&Double Freeする
3. 50,51でtcacheに2つ空きを作る
4. 56でfastbinからチャンクを一つ取り、fastbinの末尾から二つをtcacheへ移動
5. __free_hookをsystemにして、freeする


## binとチャンク
### 44行目処理後のbin
```python
43: for i in range(7):
43:    sell(i)
```
```
tcache -> chunk -> chunk -> ... -> chunk (7つ)
```

### 48行目処理後のbin
```python
46: sell(a)
47: sell(b)
48: sell(a)
```
```
tcache  -> chunk -> chunk -> ... -> chunk (7つ)
fastbin -> chunk(A) -> chunk(B) -> chunk(A) -> ...
```

### 51行目処理後のbin
```python
50: malloc(0xdeadbeef)
51: malloc(0xdeadbeef)
```
tcacheは5つ
```
tcache  -> chunk -> chunk -> chunk -> chunk -> chunk -> NULL 
fastbin -> chunk(A) -> chunk(B) -> chunk(A) -> ...
```

### 56行目処理後のbin
```python
calloc(libc.symbols.__free_hook)
```
#### fastbinのチャンク移動前
```
tcache  -> chunk -> chunk -> chunk -> chunk -> chunk -> NULL 
fastbin -> chunk(B) -> chunk(A) -> __free_hook
```
#### fastbinのチャンク移動後
#### 1個目の移動
(__free_hookの中は0, (NULL))  
```
tcache  -> __free_hook -> NULL
fastbin -> chunk(B) -> chunk(A) -> __free_hook
```
#### 2個目の移動
50,51行目ではtcacheを二つしか利用していないため、移動するチャンクも2つ(tcacheは各サイズ最大7個)  
```
tcache  -> chunk(A) -> __free_hook -> NULL
fastbin -> chunk(B) -> NULL
```

<br>

mallocを途中で3回行っていたらchunk(B)も移動する。  
fastbinからtcacheの移動は末尾のチャンクからなので(多分)  
1. __free_hook
2. chunk(A)
2. chunk(B)
という順番になる。  
