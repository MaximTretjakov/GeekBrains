"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Data:

    @classmethod
    def normalize(cls, calendar_date):
        date, month, year = calendar_date.split('-')
        return int(date), int(month), int(year)

    @staticmethod
    def validate(d, m, y):
        if 1 <= d <= 31 and 1 <= m <= 12 and 1900 <= y <= 3000:
            return f'{d} - {m} - {y}'
        else:
            return f'Введенная дата лежит вне диапазона | 1 <= {d} <= 31 | 1 <= {m} <= 12 | 1900 <= {y} <= 3000'


if __name__ == '__main__':

    while True:
        try:
            user_data = input('Введите дату в формате день-месяц-год. stop - завершение ввода.\n')
            if user_data == 'stop':
                break
            _d, _m, _y = Data.normalize(user_data)
            print(Data.validate(_d, _m, _y))
        except ValueError as er:
            print(f'Неправильно введеное значение')
