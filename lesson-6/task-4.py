"""
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
from time import sleep


class Car:
    def __init__(self):
        self.speed = 0
        self.color = 'unknown_color'
        self.name = 'unknown'
        self.is_police = False

    @staticmethod
    def go():
        return 'машина поехала...'

    @staticmethod
    def stop():
        return 'машина остановилась...\n'

    @staticmethod
    def turn(direction):
        return f'машина повернула {direction}'

    def show_speed(self):
        return self.speed


class TownCar(Car):
    max_speed = 60

    def show_speed(self):
        if TownCar.max_speed > self.speed:
            return f'вы превышаете скорость {self.speed}'


class SportCar(Car):
    def __init__(self, transmission, engine, max_speed):
        super().__init__()
        self._transmission = transmission
        self._engine = engine
        self._max_speed = max_speed

    def specifications(self):
        return f'характеристики спорт кара {self._transmission}, {self._engine}, {self._max_speed}'


class WorkCar(Car):
    max_speed = 40

    def show_speed(self):
        if WorkCar.max_speed > self.speed:
            return f'вы превышаете скорость {self.speed}'


class PoliceCar(Car):
    def __init__(self, is_police):
        super().__init__()
        self.is_police = is_police

    @staticmethod
    def goal():
        return 'задача полицейской машины выезжать на происшествия'

    @staticmethod
    def radio():
        return 'Всем постам!!! По садовому мчится красный спорт кар! Принять меры к задержанию!'


if __name__ == '__main__':

    tc = TownCar()
    tc.color = 'синий'
    tc.name = 'toyota'
    print(f'марка {tc.name}, цвет {tc.color}')
    tc.speed = 30
    print(tc.go())
    print(f'скорость {tc.speed}')
    tc.max_speed = 80
    print(tc.show_speed())
    print(tc.turn('на лево'))
    print(tc.stop())

    sleep(5)

    wc = WorkCar()
    wc.color = 'серобуромалиновый'
    wc.name = 'ГАЗель'
    print(f'марка {wc.name}, цвет {wc.color}')
    wc.speed = 10
    print(wc.go())
    print(f'скорость {wc.speed}')
    wc.max_speed = 45
    print(wc.show_speed())
    print(wc.turn('на право'))
    print(wc.stop())

    sleep(5)

    sp = SportCar('mechanica', 'V8', '300')
    sp.color = 'красный'
    sp.name = 'infinity'
    print(f'характеристики {sp.specifications()}')
    print(f'марка {sp.name}, цвет {sp.color}')
    sp.speed = 20
    print(sp.go())
    print(f'скорость {sp.speed}')
    sp.speed = 190
    print(sp.show_speed())
    print(sp.turn('на право'))
    print(sp.turn('на лево'))
    print(sp.stop())

    sleep(5)

    pc = PoliceCar(True)
    pc.color = 'красный'
    pc.name = 'MUSTANG'
    print(f'марка {pc.name}, цвет {pc.color}')
    pc.speed = 20
    print(pc.go())
    print(f'скорость {pc.speed}')
    pc.speed = 100
    print(pc.show_speed())
    print(pc.radio())
    print(pc.turn('на право'))
    print(pc.turn('на лево'))
    print(pc.stop())
