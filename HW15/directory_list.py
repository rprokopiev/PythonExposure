import os
import log
from pathlib import Path
from collections import namedtuple

ObjectData = namedtuple('ObjectData', ['object_name', 'object_extention', 'directory_flag', 'parent_directory_name'])
'''
ObjectData a subclass representing data of a directory / file as follow:

[
[0] - (class) str - directory / file name;

[1] - (class) str - extention of the file ('0' if ObjectData represents directory);

[2] - (class) str - '1' - if ObjectData represents directory,
                    '0' - if ObjectData represents file;

[3] - (class) str - name of the parent directory
].
'''


def get_directory_content(dir_path: Path) -> list:
    '''Method returning the tree of a directory.

    Parameter: 
        (class) Path - directory system path.

    Returns: 
        class (list) of tuples, each tuple repesent the data as follow:
            (
            [0] (class) str. - represents Directory/File path
            [1] (class) list - list of enclosed directorie names
            [2] (class) list - list of enclosed file names
            ).
    '''
    result = []
    for i in os.walk(dir_path):
        result.append(i)
    return result


def get_directory_ObjectData(dir: str, parent_dir: str) -> namedtuple:
    '''Method returning directory data.

    Parameter:  
            (class) Path - directory system path,
            (class) str - directory name,
            (class) str - parent directory name

    Returns:    
            (variable) ObjectData
    '''
    result = ObjectData(dir, '0', '1', parent_dir)
    return result


def get_file_ObjectData(file: str, parent_dir: str) -> list:
    '''Method returning file data.

    Parameter:  
            (class) Path - file system path,
            (class) str - directory name,
            (class) str - parent directory name

    Returns:    
            (variable) ObjectData
    '''
    result = ObjectData(file.split('.')[0], file.split('.')[-1], '0', parent_dir)
    return result


def directory_content_list(dir_path):
    '''Method returning data of a directory tree.

    Parameter:  
            (class) Path - filesystem path of the directory.

    Returns:    
            (class) list - list of ObjectData variables.
    '''
    result = []
    for i in get_directory_content(dir_path):
        i_path = i[0]
        if len(i[1]) > 0:
            for j in i[1]:
                result.append(get_directory_ObjectData(j, i_path.split('\\')[-1]))
                log.logger.info(msg=f'Directory "{j}" added')
        if len(i[2]) > 0:
            for j in i[2]:
                result.append(get_file_ObjectData(j, i_path.split('\\')[-1]))
                log.logger.info(msg=f'File "{j}" added')
    return result
