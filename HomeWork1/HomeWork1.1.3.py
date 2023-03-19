# Напишите программу, которая на входе получает имя пользователя, cохраняет его в переменную user_name и
# выводит строку  "Hello {user_name}!"
user_name = input('Enter your name: ')
print('Hello ', user_name, '!', sep='')
print(f'Hello {user_name}!')
print('Hello ' + user_name + '!')