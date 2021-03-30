import argparse
from pathlib import Path
from .assist import get_path

class cli:
    def __init__(self):
        local_path = get_path()
        arg_parser = argparse.ArgumentParser(description='Cli-cli !!!')
        arg_parser.add_argument('template', 
                                type=open, 
                                help='path to template'
                               )
        arg_parser.add_argument('result', 
                                type=Path,
                                nargs='?', 
                                help='path to the folder with the result',
                                default=f'{local_path}/artifact/',)
        arg_parser.add_argument('env', 
                                type=str, 
                                nargs='?',
                                help='env from the template',
                                default='123')
        args = arg_parser.parse_args()
        for arg in args._get_kwargs():
            print(str(arg[0])+' - '+str(arg[1]))
