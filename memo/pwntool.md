# pwntoolメモ

## example
```python
from pwn import *

if args.REMOTE:
    p = remote("example.com", 10000)
else:
    p = process("./a.out")

p.recvuntil(":")

payload = "A"

p.send(payload)
p.interactive()
```
```
$ python3 example.py REMOTE // リモート
$ python3 example.py        // ローカル
```

## 初期化, attach
### local 
```python
p = process("./a.out")
```

### remote
```python
io = remote("example.com", 10000)
```

## データの受信
### recv(n)
nバイト受け取る
```python
data = p.recv(8)
```

### recvall()
出力を全て受け取る
```python
data = p.recvall()
```

### recvline()
改行コードまで出力を受け取る
```python
line = p.recvline(8)
```

### recvuntil("hoge")
"hoge"という文字列までを受け取る
```python
line = p.recvuntil("input:")
line = p.recvuntil(":")
```

## データの送信
### send(str)
strを送信する
```python
p.send("hoge")
```

### sendline(str)
strを送信する(末尾に改行)
```python
p.sendline("hoge")
```

## 対話
### interactive()
```python
p.interactive()
```

## 変換
### p32(n), p64(n)
```python
p32(0xdeadbeef) # b'\xef\xbe\xad\xde'
p64(0xdeadbeef) # b'\xef\xbe\xad\xde\x00\x00\x00\x00'
```

## shellcode
shellcode生成  
```python
shellcraft.sh()
```
送信する際はasmと組み合わせる  
```
shellcode = asm(shellcraft.sh())
p.send(shellcode)
```

