# Задание 2.5.
# Напишите программу-калькулятор, которая принимает два числа и оператор (в формате str),
# производит заданное арифметическое действие и печатает результат в формате: {num1} {operator) {num2) = {result}

not_number = 'Введено не число или разделитель не точка'
try:
    num1 = float(input('Число 1: '))
except ValueError:
    print(not_number)
    exit()
try:
    num2 = float(input('Число 2: '))
except ValueError:
    print(not_number)
    exit()
operator = input('Оператор: ')
if operator not in '+-*/':
    print('Введен не верный оператор')
elif operator == '+':
    result = num1 + num2
    print(f'{num1} {operator} {num2} = {result}')
elif operator == '*':
    result = num1 * num2
    print(f'{num1} {operator} {num2} = {result}')
elif operator == '-':
    result = num1 - num2
    print(f'{num1} {operator} {num2} = {result}')
elif operator == '/':  # and num2 != 0:
    try:
        result = num1 / num2
        print(f'{num1} {operator} {num2} = {result}')
    except ZeroDivisionError:
        print('Делить на ноль нельзя')
#print(f'{num1} {operator} {num2} = {result}')