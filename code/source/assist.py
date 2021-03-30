from sys import platform
from os.path import abspath
from inspect import getsourcefile

def get_path():
    """
    возвращает путь к дирректории с этим файлом
    """
    if platform == "win32":
        separator = '\\'
    else:
        separator = '/'
    this_file = abspath(getsourcefile(lambda: None))
    array_file = this_file.split(separator)
    del array_file[-1]
    path = separator.join(array_file)
    return path + separator