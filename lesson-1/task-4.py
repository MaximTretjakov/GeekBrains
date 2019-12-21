"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""


def biggest_dec():
    print(f'Наберите команду stop для выхода из режима ввода.\n')

    while True:
        data = input()
        if data == 'stop': break
        else: print(max(','.join(data).split(',')))


if __name__ == '__main__':
    biggest_dec()
