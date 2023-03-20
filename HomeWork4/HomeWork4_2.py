# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer
def hit(**kwargs):
    for i in kwargs:
        print(f'{i}: {kwargs[i]}')


film = {"title": "Аватар",
        "director": "Джеймс Кэмерон",
        "year": 2009,
        "budget": '$237000000',
        "main_actor": "Сэм Уортингтон",
        "slogan": "Это новый мир"}
hit(**film)
