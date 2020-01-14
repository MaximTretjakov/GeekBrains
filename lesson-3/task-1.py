"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def divider(_a: int, _b: int):
    try:
        print(f'\nРезультат : {_a / _b:.2f}')
    except ZeroDivisionError as er:
        print(f'\n[ error: {er} ]')


if __name__ == '__main__':
    try:
        while True:
            a, b = [int(x) for x in input("\nВведите 2 числа через пробел. Пустой ввод для выхода.\n\n").split()]
            divider(a, b)
    except ValueError as e:
        print('\nЗавершение работы.')
