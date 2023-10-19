import numpy as np


class Matrix:
    data = None

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for j in range(rows)] for i in range(cols)]

    def __eq__(self, other) -> bool:
        return self.rows == other.rows & self.cols == other.cols

    def __add__(self, other):
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] += (self.data[i][j] + other.data[i][j])
        return result

    def __mul__(self, other):
        result = Matrix(self.rows, other.cols)
        result.data = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.cols)) for j in range(other.cols)] for i in range(self.rows)]
        return result

    def __str__(self):
        return '\n'.join([' '.join(['{:}'.format(item) for item in row]) for row in self.data])

    def __repr__(self):
        return f'Matrix({self.rows}, {self.cols})'


# Создаем матрицы
matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]

# Выводим матрицы
print(matrix1)

print(matrix2)

# Сравниваем матрицы
print(matrix1 == matrix2)

# Выполняем операцию сложения матриц
matrix_sum = matrix1 + matrix2
print(matrix_sum)

# Выполняем операцию умножения матриц
matrix3 = Matrix(3, 2)
matrix3.data = [[1, 2], [3, 4], [5, 6]]

matrix4 = Matrix(2, 2)
matrix4.data = [[7, 8], [9, 10]]

result = matrix3 * matrix4
print(result)
