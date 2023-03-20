def func_sum(number1, number2):
    return number1 + number2


def func_minus(number1, number2):
    return number1 - number2


def func_increase(number1, number2):
    return number1 * number2


def func_division(number1, number2):
    try:
        return number1 / number2
    except ZeroDivisionError:
        print('Делить на ноль нельзя')
