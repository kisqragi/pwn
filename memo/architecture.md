# systemcall

## syscall 呼び出し

### 32bit
引数をレジスタ、足りない分はスタックへ設定し、`int 0x80`。  
example:
```
.intel_syntax noprefix
.global main
main:
    mov eax, 1
    mov ebx, 1
    int 0x80
```

### 64bit
引数を設定してsyscall
```
.intel_syntax noprefix
.global main
main:
    mov rax, 60
    mov rdi, 1
    syscall
```

## 引数とレジスタ
|  | x86 | x64 |
| :--- | :---: | ---: |
| 第１引数 | ebx | rdi |
| 第２引数 | ecx | rsi |
| 第３引数 | edx | rdx |
| 第４引数 |  | r10 |
| 第５引数 |  | r8 |
| 第６引数 |  | r9 |

※ システムコールではなく通常の関数呼び出しの場合  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;４引数はr10ではなくrcxレジスタを使う。  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;また、x86の関数呼び出しの場合、引数は全てスタックに積む。  

## システムコール番号

### ausyscall
#### Install
```
$ sudo apt install -y auditd
```
#### 使用方法
##### x64
```
$ ausyscall --dump
Using x86_64 syscall table:
0	read
1	write
2	open
3	close
    ...
```

```
$ ausyscall write
write              1
pwrite             18
    ...
```

##### x86
```
$ ausyscall i386 --dump
$ ausyscall i386 write
```

