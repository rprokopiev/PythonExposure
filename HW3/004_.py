'''
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
Достаточно вернуть один допустимый вариант. 
*Верните все возможные варианты комплектации рюкзака.
'''
# from decimal import Decimal
# import decimal

# decimal.getcontext().prec = 1

LOWEST_GOOD = 0.1

hike_goods = dict(нож=0.3, вода=5.0, компас=0.2,
                  палатка=10.0, топор=2.5, сухпаек=3.0,
                  спички=0.1, одежда=3.0, посуда=4.0,
                  )

max_load = int(input('Введите максимальную грузоподъёмность: '))
load_dict = dict()

while max_load > LOWEST_GOOD:
    for key, value in hike_goods.items():
        if value < max_load:
            if load_dict.setdefault(key) == None:
                load_dict[key] = 1
            else:
                load_dict.update(dict([(key, (load_dict[key] + 1))]))
            max_load = max_load - value

print(f'В рюкзак поместятся следующие предметы:\n {load_dict}')
