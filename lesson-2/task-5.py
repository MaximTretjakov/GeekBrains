"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
"""


def rating():
    rating_list = [7, 5, 3, 3, 2]
    print(f'\nТекущий рейтинг {rating_list}')

    while True:
        data = input('Введите новый элемент рейтинга натуральное число\n')
        if data == 's' or len(data) == 0: break
        if int(data) not in rating_list:
            rating_list.append(int(data))
        else:
            rating_list.insert(rating_list.index(int(data)) + 1, int(data))

        print(f'\nРейтинг : {list(reversed(sorted(rating_list)))}')


if __name__ == '__main__':
    rating()
