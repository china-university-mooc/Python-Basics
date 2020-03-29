# 字典创建
print('===字典创建')

d = {'中国':'北京', '美国':'纽约'}
print(d)

d = {}
print(d)

d = dict()
print(d)

# 字典操作函数和方法
print('===字典操作函数和方法')

d = {'中国':'北京', '美国':'纽约'}
del d['美国']
print(d)

d = {'中国':'北京', '美国':'纽约'}
print('中国' in d)

print(d.keys())
print(d.values())
print(d.items())

print(d.get('韩国', '默认值'))
print(d.pop('韩国', '默认值'))

print(d.popitem())

print(len(d))

d.clear()
print(d)