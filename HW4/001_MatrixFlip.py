'''
Напишите функцию для транспонирования матрицы
'''


def even_matrix_transpose(a):
    for i in range((len(a))):
        for j in range(i, (len(a[0]))):
            tmp = a[j][i]
            a[j][i] = a[i][j]
            a[i][j] = tmp


a = [[1, 2, 3], [7, 8, 9], [10, 11, 12]]

print(f'{a[0]} \n{a[1]} \n{a[2]} \n')

even_matrix_transpose(a)

print(f'{a[0]} \n{a[1]} \n{a[2]} \n')
