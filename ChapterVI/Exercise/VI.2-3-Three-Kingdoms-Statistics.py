import jieba

def getText():
    with open('threekingdoms.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    return text

def getWords(text):
    return jieba.lcut(text, cut_all=False)

def countWord(words):
    counts = {}
    for word in words:
        if len(word) <= 1 or word in excludes:
            continue
        if word == '孔明曰' or word == '孔明':
            word = '诸葛亮'
        elif word == '玄德曰' or word == '玄德':
            word = '刘备'
        elif word == '丞相':
            word = '曹操'
        elif word == '云长' or word == '关公':
            word = '关羽'
        elif word == '都督':
            word = '周瑜'

        counts[word] = counts.get(word, 0) + 1
    return counts

excludes = ['将军', '却说', '二人', '不可', '荆州', '不能', '如此', 
'商议', '如何', '主公', '军士', '左右', '军马', '引兵', '次日', '大喜', 
'天下', '东吴', '于是', '今日', '不敢', '魏兵', '陛下', '一人', '人马', 
'不知', '汉中', '只见', '众将']
words = getWords(getText())
counts = countWord(words)

items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(10):
    if (i < len(items)):
        word, count = items[i]
        print("{:<6}:{:>5}".format(word, count))