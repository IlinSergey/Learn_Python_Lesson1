# Задание 1
def get_summ(one, two, delimiter='&'):
    return str(one) + delimiter + str(two)
result = get_summ('Learn', 'Python')
print(result.upper())
