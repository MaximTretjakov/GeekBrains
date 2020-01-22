"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

from functools import reduce


def less_then():
    minimum_salary = 20000
    salary_list = []
    less_then_list = []

    with open('../lesson-5/task-3.txt', 'r') as fd:
        for line in fd:
            surname, salary = line.split()
            salary_list.append(int(salary))
            if int(salary) < minimum_salary:
                less_then_list.append(f'зарплата сотрудника {surname} ниже {minimum_salary}')

    average_salary = reduce(lambda a, b: a + b, salary_list) / len(salary_list)
    return average_salary, less_then_list


if __name__ == '__main__':
    with open('../lesson-5/task-3.txt', 'a+') as f:
        while True:
            data = input('Запишите фамилии сотрудников и величину их окладов. stop - завершить ввод\n')
            if data == 'stop':
                break
            f.write(data + '\n')

    av_salary, less_then_min = less_then()
    print(f'{less_then_min}')
    print(f'Средняя зарпалата {int(av_salary)}')
