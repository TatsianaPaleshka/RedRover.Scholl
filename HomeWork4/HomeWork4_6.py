# 4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.
import my_calc
num1, num2 = int(input('Введите число 1: ')), int(input('Введите число 2: ')),
print(f'Сложение чисел: {my_calc.func_sum(num1, num2)}')
print(f'Вычитание чисел: {my_calc.func_minus(num1, num2)}')
print(f'Умножение чисел: {my_calc.func_increase(num1, num2)}')
print(f'Деление чисел: {my_calc.func_division(num1, num2)}')
