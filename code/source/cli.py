import argparse
from pathlib import Path
from .assist import get_path, load_file
from os.path import exists, join


class cli:
    """
    точка входа для командной строки
    """

    def __init__(self):
        local_path = get_path()
        arg_parser = argparse.ArgumentParser(description='Cli-cli !!!')
        arg_parser.add_argument('template',
                                type=Path,
                                help='path to template'
                                )
        arg_parser.add_argument('-r',
                                metavar='result',
                                type=Path,
                                nargs='?',
                                help='path to the folder with the result [default ./artifact/]',
                                default=join(f'{local_path}','artifact'))
        arg_parser.add_argument('-e',
                                metavar='env',
                                type=str,
                                nargs='?',
                                help='env from the template (path to yaml file or even on the cli) [default ./templatefile.env]',
                                default='')
        self._args = arg_parser.parse_args()
        # обработка аргумента template
        finding_template = f'{str(self._args.template)}.env'
        if exists(finding_template):
            template = finding_template
        else:
            template = join(local_path,'template', finding_template)
        # обработка аргумента -е
        # если аргумент пустой выполняем поиск по имени файла + расширение (.env)
        # если нет, предпологаем что указан путь до файла, пытаемся прочитать
        # если не читается предпологаем что данные переданы в формате командной строки по этому передаём управление дальше
        if not self._args.e:
            try:
                self._args.e = load_file(template)
            except FileNotFoundError as err:
                print(err)
                raise
        else:
            try:
                self._args.e = load_file(self._args.e)
            except FileNotFoundError as err:
                print(err)

    def get_arg(self, name_arg):
        """
        получить значение параметра по имени
        """
        return self._args.__dict__[name_arg]
