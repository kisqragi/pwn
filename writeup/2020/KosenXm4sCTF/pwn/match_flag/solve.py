from pwn import *

pattern = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_!"#$%&\'()*+,-./:;<=>?@[\\]^`|}'

s = 'xm4s{'

f = True 
while f:
    for c in pattern:
#        p = remote('27.133.155.191', 30009)
        p = remote('153.125.225.197 30009', 30009)
        p.sendline(s+c)
        ret = p.recvline()
        log.warn(s)
        if 'Correct' in str(ret):
            s += c
            log.warn('flag : ' + s)
            if c == '}':
                f = False
            break
    else:
        f = False
