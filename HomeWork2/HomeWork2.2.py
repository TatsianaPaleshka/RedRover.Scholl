# Задание 2.2
# Напишите программу, которая проверяет является ли введенное число четным.
# Если да, выведите на экран текст “Четное”, а иначе - “Нечетное”

num = int(input('Число: '))
if num % 2 == 0:
    print('Четное')
else:
    print('Нечетное')