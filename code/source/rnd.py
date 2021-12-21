from jinja2 import BaseLoader, TemplateNotFound, Environment
from os import walk, mkdir
from os.path import join, exists, getmtime
from .assist import get_path, load_file


class rndException(Exception):
    pass


class _loader(BaseLoader):
    """
    загрузчик шаблона
    """

    def __init__(self, path):
        self.path = path

    def get_source(self, environment, template):
        path = join(self.path, template)
        source = load_file(path)
        mtime = getmtime(path)
        return source, path, lambda: mtime == getmtime(path)


class rnd():
    """
    Класс генерирует файлы по шаблону
    """

    def __init__(self, path_result, dir_tamplate = ''):
        _path = get_path()

        # размечаем окружение
        if not exists(path_result):
            mkdir(path_result)
        self._pathOut = path_result
        default_dir = join(_path, 'template')
        if not dir_tamplate or dir_tamplate == default_dir:
            self._pathTemplate = default_dir
            if not exists(self._pathTemplate):
                mkdir(self._pathTemplate)
        elif exists(dir_tamplate):
            self._pathTemplate = dir_tamplate
        else:
            raise rndException(f'Папка с шаблонами {dir_tamplate} не найдена')
        loader_template = _loader(self._pathTemplate)
        self._environment = Environment(loader=loader_template)


    def cast_template(self, source_template):
        """
        задаёт шаблон
        """
        directory_template = next(walk(self._pathTemplate))
        if exists(source_template):
            loader_template = _loader(self._pathTemplate)
            env = Environment(loader=loader_template)
            return env.get_template(source_template)
        elif source_template in directory_template[2]:
            return self._environment.get_template(source_template)
        else:
            raise rndException(f'шаблон {source_template} не найден')

    def cast_variable(self, dict_vars):
        """
        передать словарь с переменными шаблона
        """
        #предполагается проверка содержимого
        if type(dict_vars) is dict:
            return dict_vars
        else:
            raise rndException(f'метод cast_variable принимает только dict')

    def _go_render(self, vars, template):
        """
        внутренний метод. Рендерит текст в память из шаблона
        """
        return template.render(vars)

    def cast_file( self, f_name_result, template, vars=''):
        """
        записать результат на диск
        """
        with open(join(self._pathOut, f_name_result), 'w+') as new_file:
            new_file.write(self._go_render(vars, template))
