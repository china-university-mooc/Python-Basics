import jieba

# 精确匹配和全模式
s = '中国是一个伟大的国家'
print(jieba.lcut(s))
print(jieba.lcut(s, cut_all=True))

# 搜索引擎模式
s = '中华人名共和国是伟大的'
print(jieba.lcut_for_search(s))

# 添加新的分词
s = '蟒蛇语言是最好的语言'
print(jieba.lcut(s))
jieba.add_word('蟒蛇语言')
print(jieba.lcut(s))