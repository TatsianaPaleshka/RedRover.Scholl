# 4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра
import time


def decorator_perf(func):
    def wrapper(arg):
        time_start = time.perf_counter()
        func(arg)
        time_end = time.perf_counter()
        print('Таймеры старта и окончания', time_start, time_end)
        print('Время выполнения функции', time_end - time_start)
    return wrapper


@decorator_perf
def square(side):
    _perimetr = side * 4
    _square = side ** 2
    _diagonal = side * 2 ** 0.5
    print(f'Сторона квадрата: {side} и его - Периметр: {_perimetr}, Площадь: {_square}, Диагональ: {_diagonal}')


square(3)
