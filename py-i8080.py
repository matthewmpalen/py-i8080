# Python
from argparse import ArgumentParser

# Local
from core.systems import Intel8080System

def main():
    arg_parser = ArgumentParser()
    arg_parser.add_argument('filename', help='ROM file')
    args = arg_parser.parse_args()

    filename = args.filename

    system = Intel8080System(filename)
    system.boot()

if __name__ == '__main__':
    main()
