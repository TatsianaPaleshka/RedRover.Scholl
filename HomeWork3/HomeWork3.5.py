# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение

film = {"title": "Аватар",
        "director": "Джеймс Кэмерон",
        "year": 2009,
        "budget": '$237000000',
        "main_actor": "Сэм Уортингтон",
        "slogan": "Это новый мир"}
print(film.keys())
print(film.values())
print(film.items())