ls = [1, 2, 5, 0]
"""
all(), any()
hash(), id() 哈希和内存地址
reversed(), sorted()  逆序和排序
type() 返回类型
"""
print(all(ls))
print(any(ls))
print(hash('中国梦'))
print(id(ls))
print(list(reversed(ls)))
print(sorted(ls))
print(sorted(ls, reverse=True))
print(type(ls))