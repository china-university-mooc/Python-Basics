def reverse(str):
    if (str == ''):
        return str
    return str[1:] + str[0]

print(reverse(''))
print(reverse('a'))
print(reverse('abc'))