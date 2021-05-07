import argparse
from pathlib import Path, PosixPath
from .assist import get_path, load_file
from os.path import exists, join, dirname, basename


class cli:
    """
    точка входа для командной строки
    """

    def __init__(self):
        self.local_path = get_path()
        arg_parser = argparse.ArgumentParser(description='Cli-cli !!!')
        arg_parser.add_argument('template',
                                type=str,
                                help='path to template'
                                )
        arg_parser.add_argument('-r',
                                metavar='result',
                                type=str,
                                nargs='?',
                                help='path to the folder with the result [default ./artifact/]',
                                default=join(f'{self.local_path}','artifact'))
        arg_parser.add_argument('-e',
                                metavar='env',
                                type=str,
                                nargs='?',
                                help='env from the template (path to yaml file or even on the cli) [default ./templatefile.env]',
                                default='')
        self._result_dict = {}
        self._args = arg_parser.parse_args()
        # обработка аргумента template
        path, name_file = self._normalize_path(self._args.template)
        self._result_dict['dir_template'] = path
        self._result_dict['file_template'] = name_file

        self._result_dict['dir_result'] = self._args.r

        #if exists(join(path,name_file)):
        #    finding_template = str(self._args.template)
        #if exists(finding_template):
        #    template = finding_template
        #else:
        #    template = join(self.local_path,'template', finding_template)

        # обработка аргумента -е
        # если аргумент пустой выполняем поиск по имени файла + расширение (.env)
        # если нет, предпологаем что указан путь до файла, пытаемся прочитать
        # если не читается предпологаем что данные переданы в формате командной строки по этому передаём управление дальше
        if not self._args.e:
            try:
                self._result_dict['env_stream'] = load_file(join(self._result_dict['dir_template'], self._result_dict['file_template']+'.env'))
            except FileNotFoundError as err:
                print(err)
                raise
        else:
            try:
                self._result_dict['env_stream'] = load_file(self._args.e)
            except FileNotFoundError as err:
                print(err)
                self._result_dict['env_stream'] = self._args.e
    def _normalize_path(self, value: Path):
        '''
        Проверяем путь до файла и возвращаем отдельно имя файла и путь
        '''
        if exists(value):
            return dirname(value), basename(value)
        elif exists(join(self.local_path,'template', value)):
            default_path = join(self.local_path,'template', value)
            return dirname(default_path), basename(default_path)
        else:
            print(f'file {value} not found')
            raise




    
    def get_arg(self, name_arg):
        """
        получить значение параметра по имени
        """
        return self._result_dict[name_arg]
