try:
    d = eval(input())
    o = {}
    for key,value in d.items():
        o[value] = key

    print(o)
except (AttributeError, NameError):
    print('输入错误')