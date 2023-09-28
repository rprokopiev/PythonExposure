'''
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. 
Результаты обхода сохраните в файлы json, csv и pickle.
    ○ Для дочерних объектов указывайте родительскую директорию.
    ○ Для каждого объекта укажите файл это или директория.
    ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
'''
import os
from pathlib import Path


DIR_PATH = Path().cwd() / 'task_folder'
PARENT_DIR_NAME = 'task_folder'
OBJECT_TYPES = ['Directory', 'File']


def get_directory_content(dir_path: Path) -> list:
    result = []
    for i in os.walk(dir_path):
        result.append(i)
    return result


def get_directory_size(dir_path: Path) -> int:
    result = 0
    for d_path, _, files in os.walk(dir_path):
        for file in files:
            result += os.path.getsize(os.path.join(d_path, file))
    return result


def get_file_size(f_path: Path, file: str) -> int:
    result = os.path.getsize(os.path.join(f_path, file))
    return result


def get_directory_datalist(dir_path: Path, dir: str, parent_dir: str) -> list:
    result = []
    result.append(dir)
    result.append(parent_dir)
    result.append(OBJECT_TYPES[0])
    result.append(get_directory_size(dir_path))
    return result


def get_file_datalist(f_path: Path, file: str, parent_dir: str) -> list:
    result = []
    result.append(file)
    result.append(parent_dir)
    result.append(OBJECT_TYPES[1])
    result.append(get_file_size(f_path, file))
    return result


def directory_content_list(dir_path):
    result = []
    for i in get_directory_content(dir_path):
        i_path = i[0]
        if len(i[1]) > 0:
            for j in i[1]:
                result.append(get_directory_datalist(
                    os.path.join(i_path, j), j, i_path.split('\\')[-1]))
        if len(i[2]) > 0:
            for j in i[2]:
                result.append(get_file_datalist(i_path, j, i_path.split('\\')[-1]))
    return result


print(directory_content_list(DIR_PATH))

