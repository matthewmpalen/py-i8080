# Python
import logging

# Local
from .cpu.cpus import CPU

class Intel8080System(object):
    logger = logging.getLogger('Intel8080System')

    def __init__(self, filename):
        self._CPU = CPU()

        if not filename:
            return

        try:
            with open(filename, 'rb') as f:
                self._CPU.load(f.read())
        except FileNotFoundError as e:
            Intel8080System.logger.error(e)
            exit()

    def boot(self):
        self._CPU.start()
        Intel8080System.logger.info('Booted system')

    def _get_test_suite(self):
        from unittest import TestSuite, defaultTestLoader
        import core.cpu.tests as tests1

        suite = TestSuite()

        for t in (tests1, ):
            suite.addTests(defaultTestLoader.loadTestsFromModule(t))

        return suite

    def run_tests(self):
        from unittest import TextTestRunner

        Intel8080System.logger.info('Running test suite')
        suite = self._get_test_suite()
        TextTestRunner().run(suite)

        Intel8080System.logger.info('Test suite finished')
