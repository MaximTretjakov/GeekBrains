"""
Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц)
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, matrix):
        self._matrix = matrix
        self._result = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]

    def __str__(self):
        return f'матрица {self._matrix}'

    def __getitem__(self, item):
        return self._matrix[item]

    def __add__(self, other):
        for i in range(len(self._matrix)):
            for j in range(len(self._matrix[0])):
                self._result[i][j] = self._matrix[i][j] + other[i][j]

        return Matrix(self._result)


if __name__ == '__main__':

    mtx1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

    mtx2 = [[5, 2, 1],
            [4, 5, 0],
            [3, 8, 9]]

    mtx = Matrix(mtx1)
    print(mtx)
    print(f'сложение екземпляра типа Matrix и матрицы 3 x 3 {mtx + mtx2}')

    mtx_1 = Matrix(mtx1)
    mtx_2 = Matrix(mtx2)
    print(f'сложение двух экземпляров типа Matrix {mtx_1 + mtx_2}')
