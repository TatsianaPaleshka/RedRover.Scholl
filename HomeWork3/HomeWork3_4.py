# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
str_1, str_2 = input('Famyly 1: '), input('Famyly 2: ')
family_1, family_2 = str_1.split(','), str_2.split(',')
if len(family_1) == len(family_2):
    print('Equal')
elif len(family_1) > len(family_2):
    print(family_1)
else:
    print(family_2)

