from enum import IntEnum
from enum import unique

@unique
class Regs(IntEnum):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    H = 5
    L = 6

@unique
class DRegs(IntEnum):
    PSW = 0
    BC = 1
    DE = 2
    HL = 3
    M = 4

class Register(object):
    def __init__(self, dtype):
        self._dtype = dtype
        self._value = 0xff

    def __str__(self):
        return '%s' % (self._value)
