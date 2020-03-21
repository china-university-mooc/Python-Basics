# 可选参数
print("===可选参数")
def add(a, b=1):
    return a + b
print(add(3))
print(add(3, 4))

# 可变参数
print("===可变参数")
def add(a, *b):
    for i in b:
        a += i
    return a
print(add(3))
print(add(3, 4))
print(add(3, 4, 5))

# 传参方式
print("===传参方式")
def add(a, b = 1):
    return a + b
print(add(3, 4))
print(add(b=4, a=3))

# 返回多个值
print("===返回多个值")
def add (a, b):
    return a + b, a, b

result = add(3, 4)
print(result)
a, b, c = add(3,4)
print(a, b, c)

# global 使用全局变量
print("===global 使用全局变量")
a = 3
def f():
    global a
    a = 4
f()
print(a)

# lambda 函数
print("===lambda 函数")
f = lambda x, y : x + y
print(f(3,4))
g = lambda : 'Hello'
print(g())