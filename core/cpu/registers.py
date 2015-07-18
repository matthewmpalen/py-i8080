from numpy import uint8

class Register(object):
    def __init__(self):
        self._value = uint8(0)

    def read(self):
        return self._value

    def write(self, value):
        self._value = uint8(value)

    def increment(self, value):
        if value <= 0:
            raise ValueError('Must be a positive value')

        self._value += value

    def __str__(self):
        return '%s' % (self.read())
