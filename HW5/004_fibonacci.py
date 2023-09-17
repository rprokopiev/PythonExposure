'''
Создайте функцию генератор чисел Фибоначчи (см. Википедию).
'''

def fibonacci(num):
    positive_list = [0, 1]
    for i in range(num):
        positive_list.append(positive_list[-2]+positive_list[-1])
        yield positive_list[i]


N = 10
for i, num in enumerate(fibonacci(N), start=1):
    print(f'{i}) {num}')
    
