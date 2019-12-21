"""
5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""


def profit_per_soul(profit: int):
    """
    Выручка / Численность всех работников предприятия = Выручка на одного работника
    :param profit:
    :return:
    """
    count_employee = input('Введите количество сотрудников ваше конторы\n')
    print(f'Выручка на одного сотрудника {round(profit / int(count_employee), 2)}')


def efficiency(profit: int, loss: int):
    """
    Прибыль / выручка * 100 % = рентабельность выручки
    :param profit:
    :param loss:
    :return:
    """
    print(f'Рентабельность выручки = {round(profit / (profit - loss) * 100, 2)}')


def balance():
    profit = input('Введите прибыль\n')
    loss = input('Введите убытки\n')
    if int(profit) > int(loss):
        print(f'Баланс положительный {profit}')
        efficiency(int(profit), int(loss))
        profit_per_soul(int(profit))
    else:
        print(f'баланс отрицательный {loss}')


if __name__ == '__main__':
    balance()