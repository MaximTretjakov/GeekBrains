"""
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и
умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма')
        return f'result = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение')
        return f'result = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'result = {self.a} + {self.b} * i'


if __name__ == '__main__':

    c_1 = Complex(1, -2)
    c_2 = Complex(3, 4)
    print(c_1)
    print(c_1 + c_2)
    print(c_1 * c_2)
