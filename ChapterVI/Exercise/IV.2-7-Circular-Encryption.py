
d = {}
for base in (ord('a'), ord('A')):
    for i in range(26):
        d[chr(base + i)] = chr(base + (i + 13) % 26)

inStr = input()
ls = [d.get(ch, ch) for ch in inStr]
print(''.join(ls))