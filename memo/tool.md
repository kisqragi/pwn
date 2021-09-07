# pwndocker
https://github.com/skysider/pwndocker  
## build
```sh
cd pwndocker
docker build -t pwndocker .
```
## pwndbg/setup.shでエラーを吐く場合
`/.dockerenv`が存在している必要がある。  
```sh
touch /.dockerenv
```

# patchelf
```sh
patchelf --set-rpath /path/to/lib <file>
```

# gdbserver
```sh
socat tcp-l:10000,reuseaddr,fork 'system:gdbserver localhost\:10001 ./chall'
```
```sh
nc localhost 10000
```
```sh
gdb -ex 'target remote localhost:10001' -ex 'b main'
```

# socat
```sh
socat tcp-l:10000,reuseaddr,fork system:./chall
```
