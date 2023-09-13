"""
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
где ключ — значение переданного аргумента, а значение — имя аргумента. 
Если ключ не хешируем, используйте его строковое представление.
"""


def get_dict(**kwargs):
    result = dict()
    unhash_types = ("<class 'list'>", "<class 'dict'>", "<class 'set'>")
    for key, value in kwargs.items():
        value_type = f'{type(value)}'
        if any(map(lambda x: x == value_type, unhash_types)):
            result[f'{value}'] = key
        else:
            result[value] = key
    return result


print(get_dict(cat="Tima", dog=["Rex", "Пэкс"], parrot=3.14, \
               fish=dict(one='GoldOne', two='BlackOne'), \
                rat={1, 2, 3, 4}))