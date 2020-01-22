"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from functools import reduce

if __name__ == '__main__':
    data = input('Введите числа: \n')
    with open('../lesson-5/task-5.txt', 'w') as fw:
        fw.write(data)

    with open('../lesson-5/task-5.txt', 'r') as fr:
        for line in fr:
            dec = map(int, line.split())
            print(f'Сумма чисел в файле {sum(dec)}')
