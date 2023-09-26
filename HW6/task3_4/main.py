from queen import eight_queen
from locations_generator import locations_generator

'''Задача №3'''
queens_locations = [(1, 1), (1, 2), (1, 3), (1, 4), 
                    (1, 5), (1, 6), (1, 7), (7, 8)]

print(eight_queen(queens_locations))



'''Задача №4'''
LOCATIONS_QUANTITY = 4

def find_true_locations():
    n = LOCATIONS_QUANTITY
    result = []
    tmp_list = []
    while n > 0:
        tmp_list = locations_generator()
        if eight_queen(tmp_list):
            print(tmp_list)
            result.append(tmp_list)
            n -= 1
    return result

print(find_true_locations())
