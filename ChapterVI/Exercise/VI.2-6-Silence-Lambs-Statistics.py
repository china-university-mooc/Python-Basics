import jieba

def getText():
    with open('沉默的羔羊.txt', 'r') as f:
        txt = f.read()
    return txt

def countWord(txt):
    words = jieba.lcut(txt)
    wordToCount = {}
    for word in words:
        if len(word) > 2:
            wordToCount[word] = wordToCount.get(word, 0) + 1
    return wordToCount

txt = getText()
wordToCount = countWord(txt)

ls = list(wordToCount.items())
ls.sort(key=lambda x:x[1], reverse=True)
for i in range(10):
    word, count = ls[i]
    print(word, count)