# -*- coding: utf-8 -*
"""
      ┏┓       ┏┓
    ┏━┛┻━━━━━━━┛┻━┓
    ┃      ☃      ┃
    ┃  ┳┛     ┗┳  ┃
    ┃      ┻      ┃
    ┗━┓         ┏━┛
      ┗┳        ┗━┓
       ┃          ┣┓
       ┃          ┏┛
       ┗┓┓┏━━━━┳┓┏┛
        ┃┫┫    ┃┫┫
        ┗┻┛    ┗┻┛
    God Bless,Never Bug
"""

import os
import sys
from string import Template
from getopt import getopt


class Depoly:
    """
    USAGE:
        python3 build.py -f [dockerfile] -n [image(container) name]
    """
    @staticmethod
    def _build_image(dockerfile, name):
        os.system(f'docker build -f {dockerfile} -t {name} .')

    @staticmethod
    def _format_yaml(name):
        with open('docker-compose.yaml', 'r') as f:
            value_str = Template(f.read())
        f.close()
        with open('docker-compose.yaml', 'w') as f:
            f.write(value_str.substitute(name=name))
        f.close()

    @classmethod
    def exec(cls):
        try:
            args = sys.argv
            opts, args = getopt(args[1:], 'f:n:')
            opts_dict = dict(opts)
            dockerfile = opts_dict['-f']
            name = opts_dict['-n']
        except KeyError:
            sys.exit(cls.__doc__)
        cls._build_image(dockerfile=dockerfile,
                         name=name)
        cls._format_yaml(name=name)
        os.system('docker-compose up -d')
        os.system('git checkout docker-compose.yaml')

if __name__ == '__main__':
    Depoly.exec()
