"""
2. Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""


def user_input():
    data_list = []

    while True:
        data = input('\nВведите числа. \nКоманда s завершает ввод.\n')
        if data == 's': break
        data_list.append(data)

    return data_list


def permutation(sequence, last=''):
    s = [i[::-1] for i in zip(sequence[0::2], sequence[1::2])]
    print([it for i in s for it in i] + list(last))


def main(sequence):
    if len(sequence) % 2 == 0:
        print('В списке четное количество элементов')
        permutation(sequence)
    else:
        print('В списке нечетное количество элементов')
        permutation(sequence, sequence[-1:])


if __name__ == '__main__':
    main(user_input())
