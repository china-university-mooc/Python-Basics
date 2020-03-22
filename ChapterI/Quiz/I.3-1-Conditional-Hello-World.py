def print_by(output, num):
    for i in range(0, len(output), num):
        end = i + num
        if end > len(output):
            end = len(output)

        print(output[i:end])

str = input()
num = eval(str)
ouput = 'Hello World'
if num == 0:
    print(ouput)
    ouput = ''
elif num > 0:
    print_by(ouput, 2)
else:
    print_by(ouput, 1)
