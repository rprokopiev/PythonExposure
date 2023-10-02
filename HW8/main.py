'''
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. 
Результаты обхода сохраните в файлы json, csv и pickle.
    ○ Для дочерних объектов указывайте родительскую директорию.
    ○ Для каждого объекта укажите файл это или директория.
    ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
'''
import dir_list_cerilization as dlc
import directory_list as dl
from pathlib import Path


DIR_PATH = Path().cwd() / 'task_folder'
dir_name = str(DIR_PATH).split('\\')[-1]
dir_list = dl.directory_content_list(DIR_PATH)
dlc.to_json('dir_json.json', dir_list)
dlc.to_csv('dir_csv.csv', dir_list)
dlc.to_bytefile('byte_file', dir_list)

