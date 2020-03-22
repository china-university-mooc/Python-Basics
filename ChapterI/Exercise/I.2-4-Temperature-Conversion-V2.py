 str = input()
if str[0] == 'C':
    f = eval(str[1:]) * 1.8 + 32
    print('F{:.2f}'.format(f))
else:
    c = (eval(str[1:]) - 32) / 1.8
    print('C{:.2f}'.format(c))