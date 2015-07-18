# Python
import logging

# Local
from .cpu.cpus import CPU

class Intel8080System(object):
    logging.basicConfig(level=logging.WARNING, filename='logs/py-i8080.py.log', 
            filemode='w')
    logger = logging.getLogger('Intel8080System')

    def __init__(self, filename):
        self._CPU = CPU()

        try:
            with open(filename, 'rb') as f:
                self._CPU.load(f.read())
        except FileNotFoundError as e:
            Intel8080System.logger.error(e)
            exit()

    def boot(self):
        self._CPU.start()
        Intel8080System.logger.info('Booted system')
