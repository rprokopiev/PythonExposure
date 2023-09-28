'''
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

'''
import os
from pathlib import Path

VIDEO_EXTENTIONS = ['3gp', 'avi', 'mov', 'mp4', 'm4v', 'm4a', 'mp3', 'mkv', 'ogv', 'ogm', 'ogg', 'oga', 'webm', 'wav']
VIDEO_FOLDER = 'Video'
PICTURE_EXTENTIONS = ['bmp', 'gif', 'jpg', 'jpeg', 'png', 'webp']
PICTURE_FOLDER = 'Pictures'
TEXT_EXTENTIONS = ['txt', 'md', 'docx', 'pdf']
TEXT_FOLDER = 'Text'

DIR_PATH = Path().cwd() / 'task_folder'


def check_folder_name(list_dir, folder_name):
    for item in list_dir:
        if folder_name in list_dir:
            return True
        else:
            return False
        

def files_replacement(file_name, new_dir):
    os.replace(f'{DIR_PATH}/{file_name}', os.path.join(os.getcwd(), new_dir, file_name))


def files_sorting(f_list):
    for item in f_list:
        if item.split('.')[-1].lower() in VIDEO_EXTENTIONS:
            if check_folder_name(os.listdir(), VIDEO_FOLDER):
                files_replacement(item, VIDEO_FOLDER)
            else:
                os.mkdir(VIDEO_FOLDER)
                files_replacement(item, VIDEO_FOLDER)
        elif item.split('.')[-1].lower() in PICTURE_EXTENTIONS:
            if check_folder_name(os.listdir(), PICTURE_FOLDER):
                files_replacement(item, PICTURE_FOLDER)
            else:
                os.mkdir(PICTURE_FOLDER)
                files_replacement(item, PICTURE_FOLDER)
        elif item.split('.')[-1].lower() in TEXT_EXTENTIONS:
            if check_folder_name(os.listdir(), TEXT_FOLDER):
                files_replacement(item, TEXT_FOLDER)
            else:
                os.mkdir(TEXT_FOLDER)
                files_replacement(item, TEXT_FOLDER)
        else:
            continue


files_list = os.listdir(DIR_PATH)
files_sorting(files_list)
