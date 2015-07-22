# Python
from argparse import ArgumentParser
import logging

# Local
from core.systems import Intel8080System

def main():
    arg_parser = ArgumentParser()
    arg_parser.add_argument('filename', help='ROM file')
    args = arg_parser.parse_args()

    filename = args.filename

    logging.basicConfig(level=logging.INFO, filename='logs/py-i8080.py.log', 
        filemode='w')

    system = Intel8080System(filename)
    system.boot()

if __name__ == '__main__':
    main()
