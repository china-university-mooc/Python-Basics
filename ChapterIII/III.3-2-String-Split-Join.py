s = input()
array = s.split('-')
headAndTail = array[::len(array) - 1]
print('+'.join(headAndTail))