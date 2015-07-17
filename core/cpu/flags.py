from enum import IntEnum
from enum import unique

@unique
class Flags(IntEnum):
    S = 0
    Z = 1
    P = 2
    C = 3
    AC = 4
    PAD = 5

class Flag(object):
    def __init__(self, dtype):
        self._dtype = dtype
        self._value = 0xff

    def __str__(self):
        return '%s' % (self._value)
