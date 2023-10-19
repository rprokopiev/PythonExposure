'''
📌Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.

📌Соберите информацию о содержимом в виде объектов namedtuple.

📌Каждый объект хранит: 
    - имя файла без расширения или название каталога, 
    - расширение, если это файл, 
    - флаг каталога, 
    - название родительского каталога.
    
📌В процессе сбора сохраните данные в текстовый файл используя логирование.
'''

import argparse
from directory_list import directory_content_list as dcl

parser = argparse.ArgumentParser(description='Directory tree parser')
parser.add_argument('numbers', metavar='N', type=str,
                    nargs='*', help='press some numbers')
args = parser.parse_args()

for item in dcl(args.numbers[0]):
    print(f'Name: {item[0]:<40} exention: {item[1]:<40} directory: {item[2]:<15} parent directory: {item[3]:<20}')
