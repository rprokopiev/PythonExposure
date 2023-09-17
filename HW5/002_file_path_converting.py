'''
Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. 
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
'''
file_path = 'C:/Users/task.git'

def get_file_path_name_extention(file_path):
    *other, file_name_extention = file_path.split('/')
    file_name, file_extention = file_name_extention.split('.')
    return (file_path, file_name, file_extention)                                            

print(get_file_path_name_extention(file_path))