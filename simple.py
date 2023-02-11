# Практика: Числа
a = 2
b = 0.5
print(a + b)

v = int(input('Введите число от 1 до 10: '))
print(v + 10) 

# Практика: Строки
name = 'Сергей'
print(f'Привет, {name}!')

name = input('Введите ваше имя: ')
print(f'Привет, {name}! Как дела?') 

# Практика: Приведение типов


float('1')  # 1.0
int('2.5')  # ValueError
bool(1)  # True
bool('')  # False
bool(0)  # False