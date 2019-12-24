"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""


def season():

    season_list = [
        {'зима': [12, 1, 2]},
        {'весна': [3, 4, 5]},
        {'лето': [6, 7, 8]},
        {'осень': [9, 10, 11]},
    ]

    season_dict = {
        'зима': [12, 1, 2],
        'весна': [3, 4, 5],
        'лето': [6, 7, 8],
        'осень': [9, 10, 11]
    }

    data = input('Введите месяц в виде целого числа от 1 до 12.\n')

    def get_season(month):
        print('dict -> ', ''.join([_season for _season, _month in season_dict.items() if month in _month]))
        print('list -> ', ''.join({k for i in season_list for (k, v) in i.items() if month in v}))

    get_season(int(data))


if __name__ == '__main__':
    season()
