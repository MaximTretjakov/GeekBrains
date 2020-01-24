"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationary:
    def __init__(self):
        self.title = 'канцелярская принадлежность'

    def draw(self):
        return f'Запуск отрисовки. Я {self.title}'


class Pen(Stationary):
    def draw(self):
        return f'Я производный класс с именем {self.__class__.__name__}'


class Pencil(Stationary):
    def draw(self):
        return f'Я тоже производный класс от {self.__class__.__bases__} и мое имя {self.__class__.__name__}'


class Handle(Stationary):
    def draw(self):
        return f'Тут тоже уникальное сообщение {self.__class__.__name__}'


if __name__ == '__main__':

    pen = Pen()
    print(pen.draw())

    pencil = Pencil()
    print(pencil.draw())

    handle = Handle()
    print(handle.draw())
