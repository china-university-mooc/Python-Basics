import jieba

f = open('沉默的羔羊.txt')
text = f.read()
f.close()

words = jieba.lcut(text)
counts = {}
for w in words:
    if len(w) > 2:
        counts[w] = counts.get(w, 0) + 1

l = list(counts.items())
l.sort(key=lambda x:x[1], reverse=True)
print(l[0][0])