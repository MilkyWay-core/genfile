from sys import platform
from os.path import abspath, exists
from inspect import getsourcefile


def get_path():
    """
    возвращает путь к дирректории с файлом из которого была запущена функция
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


def load_file(path_file):
    """
    осуществляет поиск файла и загрузку в память
    """
    with open(path_file) as f:
        return f.read()
