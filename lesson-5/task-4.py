"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

if __name__ == '__main__':
    rus = ['Один', 'Два', 'Три', 'Четыре']
    i = 0
    with open('../lesson-5/task-4.txt', 'r') as f, open('../lesson-5/task-4-rus.txt', 'a+') as f_rus:
        for line in f:
            numeral, *other = line.split()
            rus_numeral = rus[i] + ' ' + ' '.join(other) + '\n'
            i += 1
            f_rus.write(rus_numeral)

    print(f'Готово! проверьте файл task-4-rus.txt')
