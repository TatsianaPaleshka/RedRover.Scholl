# Задание 2.1
# Напишите программу, которая проверяет здоровье персонажа в игре.
# Если оно равно или меньше нуля, выведите на экран False, в противном случае True.
health_points = int(input('HP: '))
if health_points <= 0:
    print('False')
else:
    print('True')