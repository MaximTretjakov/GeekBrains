"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) 10(лаб)
Физкультура: 30(пр)

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
import re

if __name__ == '__main__':
    d = {}
    with open('../lesson-5/task-6.txt', 'r') as f:
        for line in f:
            key, *key_trash = tuple(line.split(':'))
            val_trash, *other = line.split()
            regexp = re.compile(u'[(а-я)]')
            count = map(int, re.sub(regexp, '', ' '.join(other)).split())
            value = sum(count)
            d[key] = value

    print(f'{d}')
