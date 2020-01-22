"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

if __name__ == '__main__':
    strings = 0
    words = 0
    with open('../lesson-5/task-2.txt', 'r') as f:
        for line in f:
            strings += 1
            words += len(line.split())

    print(f'количество строк {strings} слов {words}')
