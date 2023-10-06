'''
Напишите следующие функции:
    Нахождение корней квадратного уравнения
        ax2 + bx + c = 0
        D = b2 - 4ac
    Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
    Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
    Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
'''
import math
import csv
import json
from random import randint
from typing import Callable


CSV_NAME = 'randIntList.csv'
JSON_NAME = 'squareList.json'


def randint_zero_excluded(min: int, max: int):
    result = randint(min, max)
    if result == 0:
        while result == 0:
            result = randint(min, max)
    return result


def csv_of_ints(csv_file_name):
    '''Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.'''
    quantity = randint(100, 1001)
    result = []

    for _ in range(quantity):
        result.append(
            [randint_zero_excluded(-100, 101), randint_zero_excluded(-100, 101), randint_zero_excluded(-100, 101)])

    with open(csv_file_name, 'w') as file:
        csv_write = csv.writer(file, delimiter=',')
        csv_write.writerows(result)


def square_decor(func: Callable):
    '''Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.'''
    def wrapper(*args, **kwargs):
        result = []
        csv_of_ints(CSV_NAME)
        with open(CSV_NAME, 'r', newline='') as f:
            csv_reader = csv.reader(f, delimiter=',')
            for line in csv_reader:
                if len(line) != 0:
                    a, b, c = line
                    result.append(func(int(a), int(b), int(c)))
        return result
    return wrapper


def json_decorator(func: Callable) -> Callable:
    '''Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.'''
    def wrapper(*args, **kwargs):
        result = []
        result = func(args)
        with open(JSON_NAME, 'w', encoding='UTF-8') as file:
            # json.dump(args, indent=4, ensure_ascii=False)
            json.dump(result, file, ensure_ascii=False)

    return wrapper


@json_decorator
@square_decor
def square_equation(a: int, b: int, c: int) -> float:
    '''Нахождение корней квадратного уравнения.'''
    d = b*2 - 4*a*c
    if d > 0:
        x1 = round(((-b) + math.sqrt(d)) / (2*a), 2)
        x2 = round(((-b) - math.sqrt(d)) / (2*a), 2)
        return x1, x2
    elif d == 0:
        x = round((-b) / (2*a), 2)
        return x
    else:
        return None


square_equation()
