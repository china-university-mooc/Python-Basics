# 序列通用操作符
print('===序列通用操作符')
ls = [1, 2, 3, 4, 5, 6]
print(2 in ls)
print(2 not in ls)
S = ls + [7, 8]
print(S)
S = ls * 2
print(S)
print(ls[0])
print(ls[0:2])
print(ls[0:5:2])

# 序列通用函数和方法
print('===序列通用函数和方法')
t = (1, 2, 3, 4, 5)
print(len(t))
print(min(t))
print(max(t))
print(t.index(3))
print(t.index(3, 1, 5))
print(t.count(3))

# 元组类型创建
print('===元组类型')
t = (1, 2, 3)
print(t)
t = 'a','b', 'c'
print(t)
s = tuple('abc')
print(s)

# 列表类型创建
print('===列表类型创建')
ls = [1,2,3]
print(ls)
ls = list('abc')
print(ls)

# 列表类型操作符
print('===列表类型操作符')
ls[0] = 'd'
print(ls)

ls[1:3] = ['e', 'f', 'g']
print(ls)

ls[0:3:2] = ['i', 'i']
print(ls)

del ls[0]
print(ls)

del ls[0:3:2]
print(ls)

# 列表类型操作函数和方法
print('===列表类型操作函数和方法')
ls = [1]
print(ls)

ls.append(2)
print(ls)

L = ls.copy()
print(L)

ls.insert(1, 3)
print(ls)

ls.reverse()
print(ls)

print(ls.pop(1))

ls.remove(2)
print(ls)

ls.clear()
print(ls)