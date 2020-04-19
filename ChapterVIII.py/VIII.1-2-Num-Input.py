try:
    s = input()
    if 'j' in s:
        num = complex(s)
    elif '.' in s:
        num = float(s)
    else:
        num = int(s)
    print(num * num)
except:
    print('输入有误')
