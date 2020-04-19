# 文件的类型
tf = open('f.txt', 'rt')
print(tf.read())
tf.close()

bf = open('f.txt', 'rb')
print(bf.read())
bf.close()


# 遍历文件
f = open('a.txt')
txt = f.read()
print(txt)
f.close()

f = open('a.txt')
txt = f.read(2)
while txt != '':
    print(txt, end='')
    txt = f.read(2)
print()
f.close()

f = open('a.txt')
line = f.readline()
while line != '':
    print(line, end='')
    line = f.readline()
print()
f.close()

f = open('a.txt')
for line in f.readlines():
    print(line, end='')
print()
f.close()

f = open('a.txt')
for line in f:
    print(line, end='')
print()
f.close()

# 写入
f = open('b.txt', 'w+')
f.write('我是中国人\n')
f.writelines(['中国', '美国', '俄罗斯', '\n'])
f.seek(0)
for line in f:
    print(line)
f.close()