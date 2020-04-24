s = input()
for c in s:
    if ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z'):
        print(c, end='')
print()