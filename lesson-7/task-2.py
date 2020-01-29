"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""


from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def tissue_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, v=None):
        self._v = v

    @property
    def get_v(self):
        assert self._v is not None, 'Error! Передайте init() значение атрибута v'
        return self._v

    def tissue_consumption(self):
        return self.get_v / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, h=None):
        self._h = h

    @property
    def get_h(self):
        assert self._h is not None, 'Error! Передайте init() значение атрибута h'
        return self._h

    def tissue_consumption(self):
        return self.get_h * 2 + 0.3


if __name__ == '__main__':

    c = Coat(30)
    print(f'Нужно ткани для пальто {c.tissue_consumption():.2f}')

    # для проверки property пример искусственный конечно.
    # но предположим чел работает не в PyCharm, а в простом редакторе который не подсветит ему что он не передал
    # в init параметр
    s = Suit()
    print(f'Нужно ткани для костюма {s.tissue_consumption():.2f}')
