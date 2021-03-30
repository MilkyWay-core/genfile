import argparse
from pathlib import Path

class cli:
    def __init__(self):
        arg_parser = argparse.ArgumentParser(description='Cli-cli !!!')
        arg_parser.add_argument('template', type=open, help='path to template')
        arg_parser.add_argument('result', type=Path, help='path to the folder with the result')
        arg_parser.add_argument('env', type=str, help='env from the template')
        args = arg_parser.parse_args()
        for arg in args._get_kwargs():
            print(str(arg[0])+' - '+str(arg[1]))
