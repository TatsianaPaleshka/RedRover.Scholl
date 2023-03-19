# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'
list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
list_num = [x for x in list_1 if type(x).__name__ == 'int']
print(sum(list_num))
list_str = [x for x in list_1 if type(x).__name__ == 'str' and 'a' in x]
print(list_str)