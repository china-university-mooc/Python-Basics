# 异常处理的高级使用

try:
    num = eval(input())
    result = num ** 2
except NameError as e:
    print("输入错误: {}".format(e.args))
else:
    print(result)
finally:
    print("程序结束")