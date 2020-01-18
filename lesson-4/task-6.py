"""
6. Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
"""

import itertools


def count_func():
    for i in itertools.count(start=5, step=1):
        print(f'Шаг {i}')


def cycle_func():
    max_count = 10
    count = 0
    for i in itertools.cycle(['арбуз']):
        if count > max_count:
            break
        print(f'Шаг {count} : {i}')
        count += 1


if __name__ == '__main__':
    count_func()
    cycle_func()
