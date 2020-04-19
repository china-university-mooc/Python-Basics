f =  open('latex.log')
txt = f.read()
f.close()

counts = {}
total = len(txt)
for c in txt:
    if ord('a') <= ord(c) <= ord('z'):
        counts[c] = counts.get(c, 0) + 1

ls = list(counts.items())
ls.sort(key=lambda x: ord(x[0]))
letters = ['{}:{}'.format(i[0], i[1]) for i in ls]
print('共{}字符,{}'.format(total, ','.join(letters)))