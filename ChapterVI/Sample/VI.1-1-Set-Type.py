# 集合创建
print('===集合创建')
A = set()
print(A)
B = {'python', 123}
print(B)
C = set('python')
print(C)

# 集合操作符
print('===集合操作符')
A = {'p', 'y', 123}
B = set('pypy123')
print(A | B)
print(A & B)
print(A - B)
print(B - A)
print(A ^ B) # (A - B) | (B - A)
C = {'p', 'y'}
print(C < A)
print(C >= A)

# 集合处理方法
print('===集合处理方法')
A = set()
A.add('p')
A.add('y')
A.add(123)
A.add(1)
print(A)
A.discard('p')
A.remove('y')
print(A)
print(A.pop())
A.clear()
print(A)

A = {'p', 'y', 123}
B = A.copy()
print(len(B))
print('y' in B)
print('y' not in B)
C = set([1,2,2])
print(C)

