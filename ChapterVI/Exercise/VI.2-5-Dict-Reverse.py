d = eval(input())

l = [(value, key) for key,value in d.items()]

print(dict(l))