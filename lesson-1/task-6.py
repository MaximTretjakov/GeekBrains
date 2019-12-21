"""
6. Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
"""


def calculate_day():
    counter = 1

    a = input('Введите количество км в первый день\n')
    b = input('Введите количество км max\n')

    km_per_day = float(a)

    while km_per_day <= float(b):
        km_per_day = ((km_per_day * 0.1) + km_per_day)
        print(f'{counter}-й день : {round(km_per_day, 2)}')
        counter += 1

    print(f'Ответ: на {counter}-й день спортсмен достиг результата — не менее {round(km_per_day)} км.')


if __name__ == '__main__':
    calculate_day()