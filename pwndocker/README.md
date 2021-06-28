# build
```
$ docker build -t pwn .
```

# run
```
$ docker run --rm -it -v $(pwd):/ctf/work pwn
```

## gdbが上手く動かない(ptraceを使いたい)
```
$ docker run --cap-add=SYS_PTRACE --security-opt="seccomp=unconfined" --rm -it -v $(pwd):/ctf/work pwn
```