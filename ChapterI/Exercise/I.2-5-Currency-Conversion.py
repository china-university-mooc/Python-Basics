str = input()
if str[0:3] == 'RMB':
    u = eval(str[3:]) / 6.78
    print('USD{:.2f}'.format(u))
else:
    r = eval(str[3:]) * 6.78
    print('RMB{:.2f}'.format(r))