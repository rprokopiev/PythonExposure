'''
Создайте функцию-генератор. Функция генерирует N простых чисел, начиная с числа 2.
Для проверки числа на простоту используйте правило: 
«число является простым, если делится нацело только на единицу и на себя».
'''


def if_prime_number(a):
    '''Проверка числа, если оно простое.'''
    if a == 2: 
        return True
    if (a % 2 != 0) & (a != 1):
        for i in range(3, (a + 1), 2):
            if i == a:
                continue
            if a % i == 0:
                return False
        else:
            return True
    else:
        return False

def prime_numb_generator(n):
    '''Функция генерирует N простых чисел, начиная с числа 2.'''
    qty = 0
    num = 2
    while qty != n:
        if if_prime_number(num):
            qty += 1
            yield num
        num += 1

N = 9
for i, num in enumerate(prime_numb_generator(N), start=1):
    print(f'{i}) {num}')
