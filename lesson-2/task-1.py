"""
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""


def check_type():
    print([type(i) for i in ['qwe', [], (), {}, 1]])


if __name__ == '__main__':
    check_type()
