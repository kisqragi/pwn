# patchelf
```
$ patchelf --set-rpath /path/to/lib <file>
```

# gdbserver
```
$ socat tcp-l:10000,reuseaddr,fork 'system:gdbserver localhost\:10001 ./chall'
```
```
$ nc localhost 10000
```
```
$ gdb -ex 'target remote localhost:10001' -ex 'b main'
```

# socat
```
$ socat tcp-l:10000,reuseaddr,fork system:./chall
```
