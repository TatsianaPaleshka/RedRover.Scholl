# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.
def square(side):
    _perimetr = side * 4
    _square = side ** 2
    _diagonal = side * 2 ** 0.5
    return tuple((_perimetr, _square, _diagonal))


# print(square(3))
