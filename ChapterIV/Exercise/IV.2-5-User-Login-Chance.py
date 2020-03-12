chance = 3
while chance > 0:
    user = input()
    password = input()
    if (user == 'Kate' and password == '666666'):
        print('登录成功！')
        break
    chance -= 1
else:
    print('3次用户名或者密码均有误！退出程序。')