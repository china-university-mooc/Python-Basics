str = input()
if str[-1] in ['C', 'c']:
    f = eval(str[:-1]) * 1.8 + 32
    print('{:.2f}F'.format(f))
elif str[-1] in ['F', 'f']:
    c = (eval(str[:-1]) - 32) / 1.8
    print('{:.2f}C'.format(c))
else:
    print('输入格式错误')