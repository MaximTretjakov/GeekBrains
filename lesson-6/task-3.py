"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
(get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    def __init__(self):
        self.name = 'Ivan'
        self.surname = 'Pupkin'
        self.position = 'coder'
        self._income = {'wage': 5000, 'bonus': 5000}


class Position(Worker):
    def get_full_name(self):
        return self.name, self.surname

    def get_total_income(self):
        return self._income['wage'] * self._income['bonus']


if __name__ == '__main__':

    pos = Position()
    print(f'Полное имя - {pos.get_full_name()}')
    print(f'Доход с учетом премии - {pos.get_total_income()}')

    print(f'позиция - {pos.position}')
    print('пишем в атрибут')
    pos.position = 'reverse engineer'
    print(f'позиция после записи - {pos.position}')
