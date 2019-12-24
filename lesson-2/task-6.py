"""
6. *Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена,
количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]

Необходимо собрать аналитику о товарах.
Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.

Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""
from typing import List


def user_input() -> List:
    tmp = []
    while True:
        data = input('Введите данные о товаре.\n')
        if data == 's': break
        tmp.append(data)

    return tmp


class Goods:

    def __init__(self):
        self._storage = []
        self._auto_increment = 0
        self._keys_struct = ['название', 'цена', 'количество', 'единицы']

    def row(self, *args):
        self.counter()
        row = (self._auto_increment, dict(zip(self._keys_struct, args)),)
        self._storage.append(row)

    def printing(self):
        return self._storage

    def counter(self):
        self._auto_increment += 1

    def analytics(self):
        _name = _price = _quantity = _units = ''

        name_list = []
        price_list = []
        quantity_list = []
        units_list = []

        for row in self._storage:
            _name, _price, _quantity, _units = row[1].values()
            name_list.append(_name)
            price_list.append(_price)
            quantity_list.append(_quantity)
            units_list.append(_units)

        template = {
            'название': name_list,
            'цена': price_list,
            'количество': quantity_list,
            'единицы': units_list
        }

        return template


if __name__ == '__main__':
    storage = Goods()
    # в data список введенных юзером данных о товаре
    data_user = user_input()
    # вычитываем по 4 параметра за раз и распаковываем
    for name, price, quantity, units in zip(*[iter(data_user)] * 4):
        storage.row(name, price, quantity, units)

    print(storage.printing())
    print(storage.analytics())
