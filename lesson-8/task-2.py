"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно
обработать эту ситуацию и не завершиться с ошибкой.
"""


class CustomZeroDivisionError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'{self.message}'
        else:
            return 'CustomZeroDivisionError has been raised'


if __name__ == '__main__':
    info = 'Введите числа через пробел, 0 в делителе не приведет к падению. stop - завершение ввода.\n'

    while True:
        try:
            user_data = input(info)
            if user_data == 'stop':
                break

            divisible, divider = user_data.split()
            if int(divider) == 0:
                raise CustomZeroDivisionError

            print(f'Результат {int(int(divisible) / int(divider))}')

        except CustomZeroDivisionError as er:
            print(er)
        except ValueError as er:
            print(f'Неправильно введеное значение')
