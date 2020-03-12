# 循环的扩展用法

num = eval(input())

for i in range (2, num):
    if num % i == 0:
        print("{}不是质数".format(num))
        break
else:
    print("{}是质数".format(num))