from random import randint

MAX_QTY = 8
MIN_QTY = 1

def locations_generator():
    locations_list = []
    for i in range(MAX_QTY):
        tmp_tuple = ((randint(MIN_QTY, MAX_QTY)), (randint(MIN_QTY, MAX_QTY)))
        locations_list.append(tmp_tuple)
    return locations_list
