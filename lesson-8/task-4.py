"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""

"""
5. Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.
"""

"""
6. Продолжить работу над вторым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""


class Storage:

    def __init__(self, name, price, quantity, number_of_lists):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def reception(self):
        try:
            unit = input(f'Введите наименование\n')
            unit_p = int(input(f'Введите цену за ед\n'))
            unit_q = int(input(f'Введите количество\n'))
            unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
            self.my_store.append(unique)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных\n'

        print(f'Для выхода - exit, продолжение - enter\n')
        data = input(f'->\n')
        if data == 'exit':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Завершили работу\n'
        else:
            return Storage.reception(self)


class Printer(Storage):
    def to_print(self):
        return f'распечатано {self.numb} раз...\n'


class Scanner(Storage):
    def to_scan(self):
        return f'распечатано {self.numb} раз...\n'


class Copier(Storage):
    def to_copier(self):
        return f'распечатано {self.numb} раз...\n'


if __name__ == '__main__':

    p_1 = Printer('hp', 2000, 8, 108)
    s_2 = Scanner('Kyocera', 1200, 15, 110)
    c_3 = Copier('Xerox', 1500, 17, 15)
    print(p_1.reception())
    print(s_2.reception())
    print(c_3.reception())
    print(p_1.to_print())
    print(c_3.to_copier())
