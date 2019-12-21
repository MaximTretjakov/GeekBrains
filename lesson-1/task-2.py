"""
2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""


def seconds_to():
    minute = 60
    hour = 3600

    from datetime import datetime
    seconds = int(input('Введите ваши секунды\n'))
    print(f'Вы ввели {seconds} секунд и это: чч {seconds // hour} : мм {seconds // minute} : сс {seconds}')


if __name__ == '__main__':
    seconds_to()
