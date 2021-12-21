#!/usr/bin/env python

from source.cli import cli
from source.env import env
from source.rnd import rnd
from ast import literal_eval
"""
Точка входа программы
"""


def main():
    print('START')
    # читает агрументы командной строки
    args_cli = cli()
    # получает аргумент template
    file_template = args_cli.get_arg('file_template')
    # загружает шаблон
    caster = rnd(args_cli.get_arg('dir_result'), args_cli.get_arg('dir_template'))
    # получает аргумент e, если это файл читает и возвращает содержимое
    args_e = args_cli.get_arg('env_stream')
    if args_e:
        env_data_list = (env(args_e)).get_data()
        for env_data in env_data_list:
            # заполняет шаблон аргументами, генерирует файл с результатом
            for beetwen in env_data.range_list:
                for i in range(beetwen[0], beetwen[1]):
                    env_data.data['i'] = i
                    result_data, result_file = normalize_data(env_data, i)
                    vars = caster.cast_variable(result_data)
                    template = caster.cast_template(file_template)
                    caster.cast_file(f_name_result=result_file,vars=vars,template=template)
                    print(f'{result_file}:done')
    else:
    #если -е пустой выполняем гнерацию из шаблона без переменных
        template = caster.cast_template(file_template)
        caster.cast_file('default_result',template=template)
        print(f'default_result:done')
    print('END')



def normalize_data(data, i):
    '''
    читает имя и данные файла с переменными, добавляет инкремент если находит переменную $i$ 
    '''
    result_file = data.result_file.replace('$i$', str(i))
    # dict -> str, замена $i$ на i, str -> dict
    result_data = literal_eval(str(data.data).replace('$i$', str(i)))
    return result_data, result_file


main()
