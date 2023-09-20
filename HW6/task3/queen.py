'''
Добавьте в пакет, созданный на семинаре шахматный модуль. 
Внутри него напишите код, решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так, 
чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. 
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. 
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.'''


queens_locations = [(1, 1), (1, 2), (1, 3), (1, 4), 
                    (1, 5), (1, 6), (1, 7), (7, 8)]


BOARD_MAX = 8
BOARD_MIN = 1


def attack(queens_locations: list) -> bool:
    '''Проверка по горизонтали и вертикали.'''
    n = 0
    y = 0
    for item in queens_locations:
        for item2 in queens_locations:
            if item == item2:
                continue
            else:
                if (item[0] == item2[0]) | (item[1] == item2[1]):
                    return False
    return True


def downup_diagonal(queens_locations: list) -> bool:
    '''Проверка по диагонале снизу вверх (по линиям, где сумма координат даёт одинаковое число).'''
    max_location_sum = BOARD_MAX*2
    while max_location_sum > 0:
        count = 0
        for item in queens_locations:
            if item[0] + item[1] == max_location_sum:
                count += 1
        if count > 1:
            return False
        max_location_sum -= 1
    return True


def updown_diagonal(queens_locations: list) -> bool:
    '''Проверка по диагонале сверху вниз.'''
    tmp_list = []
    for i in range(BOARD_MIN, BOARD_MAX + 1):
        tmp_tuple = (i, BOARD_MIN)
        tmp_list = [tmp_tuple]
        count = 0
        for j in range(BOARD_MIN, BOARD_MAX + 1):
            if (tmp_tuple[0] != BOARD_MAX) & (tmp_tuple[1] != BOARD_MAX):
                tmp_tuple = ((tmp_tuple[0] + 1), (tmp_tuple[1] + 1))
                tmp_list.append(tmp_tuple)
            else:
                continue
        for item in queens_locations:
            for i in range(len(tmp_list)):
                if (item == tmp_list[i]):
                    count += 1
        if count > 1:
            return False

    tmp_list = []
    for i in range(BOARD_MIN, BOARD_MAX + 1):
        tmp_tuple = (BOARD_MIN, i)
        tmp_list = [tmp_tuple]
        count = 0
        for j in range(BOARD_MIN, BOARD_MAX + 1):
            if (tmp_tuple[0] != BOARD_MAX) & (tmp_tuple[1] != BOARD_MAX):
                tmp_tuple = ((tmp_tuple[0] + 1), (tmp_tuple[1] + 1))
                tmp_list.append(tmp_tuple)
            else:
                continue
        for item in queens_locations:
            for i in range(len(tmp_list)):
                if (item == tmp_list[i]):
                    count += 1
        if count > 1:
            return False
    return True  

