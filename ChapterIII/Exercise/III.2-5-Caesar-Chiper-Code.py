s = input()
for c in s:
    if 'A' <= c <= 'Z':
        start = ord('A')
        index = start + ((ord(c) - start + 3)%26)
        print(chr(index), end='')
    if 'a' <= c <= 'z':
        start = ord('a')
        index = start + ((ord(c) - start + 3)%26)
        print(chr(index), end='')
    else:
        print(c, end='')
print()