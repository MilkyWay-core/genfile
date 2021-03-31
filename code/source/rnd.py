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
    Класс рендерит файлы по шаблону
    """

    def __init__(self, name_tempalate):
        _path = get_path()
        self._pathOut = _path + 'artifact/'
        self._pathTemplate = _path + 'template/'
        # размечаем окружение
        if not exists(self._pathOut):
            mkdir(self._pathOut)
        if not exists(self._pathTemplate):
            mkdir(self._pathTemplate)
        self._template = self.set_template(name_tempalate)

    def set_template(self, name_tempalate):
        """
        сменить шаблон
        """
        files = next(walk(self._pathTemplate))
        if files:
            if name_tempalate in files[2]:
                loader_template = _loader(self._pathTemplate)
                env = Environment(loader=loader_template)
                template = env.get_template(name_tempalate)
                return template
            else:
                raise rndException(f'шаблон {name_tempalate} не найден')
        else:
            raise rndException('шаблоны не найдены')

    def set_variable(self, dict_vars):
        """
        передать словарь с переменными шаблона
        """
        self._dict_vars = dict_vars

    def _go_render(self):
        """
        внутренний метод. Рендерит текст в память из шаблона
        """
        return self._template.render(self._dict_vars)

    def cast_file(self, f_name_result):
        """
        записать результат на диск
        """
        with open(self._pathOut+f_name_result, 'w+') as new_file:
            new_file.write(self._go_render())
