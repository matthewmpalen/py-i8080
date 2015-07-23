# Python
from argparse import ArgumentParser
import logging

# Local
from core.systems import Intel8080System

def main():
    arg_parser = ArgumentParser()
    arg_parser.add_argument('--filename', help='ROM file')
    arg_parser.add_argument('--test', nargs='?', default=True, 
        help='Run test suite')
    args = arg_parser.parse_args()

    filename = args.filename

    logging.basicConfig(level=logging.INFO, filename='logs/py-i8080.py.log', 
        filemode='w')

    if filename:
        system = Intel8080System(filename)
        system.boot()
    elif args.test:
        system = Intel8080System(None)
        system.run_tests()

if __name__ == '__main__':
    main()
