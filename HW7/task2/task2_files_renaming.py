'''
Напишите функцию группового переименования файлов. Она должна:
✔ принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
✔ принимать параметр количество цифр в порядковом номере.
✔ принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
✔ принимать параметр расширение конечного файла.
✔ принимать диапазон сохраняемого оригинального имени. 
Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. 
Далее счётчик файлов и расширение.

example:
    incoming file name:
        example.txt
    
        arguments:
            NEW,    2,5     6       .txt
    result: NEW     xamp    0000001 .txt
            xampNEW000001.txt

'''
import os
from pathlib import Path

DIR_PATH = Path().cwd() / 'task_folder'


def counter(qty: int, count_number: int) -> str:
    result = ''
    i = qty - len(str(count_number))
    while i > 0:
        result += '0'
        i -= 1
    result += str(count_number)
    return result


def file_name_contraction(file_name: str, brakets: list) -> str:
    result = ''
    for i in range(len(file_name)):
        if (brakets[0] - 1) <= i <= (brakets[-1] - 1):
            result += file_name[i]
    return result


def name_constructor(new_name: str, old_name: str, brakets: list, 
                     qty: int, count_number: int, 
                     name_extention: str) -> str:
    result = ''
    result += file_name_contraction(old_name, brakets)
    result += new_name
    result += counter(qty, count_number)
    result += name_extention
    return result


def files_renaming(f_list: list, new_name: str, brakets: list, qty: int, name_extention: str):
    for i in range(len(f_list)):
        if len(f_list[i]) >= brakets[-1]:
            Path(f'{DIR_PATH}/{f_list[i]}').rename(f'{DIR_PATH}/{name_constructor(new_name, f_list[i], brakets, qty, i+1, name_extention)}')
        else:
            Path(f'{DIR_PATH}/{f_list[i]}').rename(f'{DIR_PATH}/{name_constructor(new_name, f_list[i], [1, len(f_list[i])], qty, i+1, name_extention)}')


files_renaming(os.listdir(DIR_PATH), 'NEW', [3, 6], 5, '.txt')