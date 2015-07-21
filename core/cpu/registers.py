from enum import IntEnum

class RegID(IntEnum):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    H = 5
    L = 6

class DRegID(IntEnum):
    BC = 1
    DE = 3
    HL = 5
    M = 5
    SP = 7
    PC = 8

class Registers(object):
    def __init__(self):
        self._items = bytearray(7)

    def get(self, id):
        return self._items[id]

    def set(self, id, value):
        self._items[id] = value & 0xff

    def increment(self, id, value):
        if value < 0:
            raise ValueError('Must be a positive value')

        self._items[id] += value

    def decrement(self, id, value):
        if value < 0:
            raise ValueError('Must be a positive value')

        self._items[id] -= value

    def get_pair(self, id):
        end = id + 2
        return int.from_bytes(self._items[id:end], byteorder='big', 
            signed=False)

    def set_pair(self, id, value):
        # Not sure if correct
        value = value & 0xff
        self._items[id] = value >> 8
        self._items[id + 1] = value & 0xff

    def increment_pair(self, id, value):
        if value < 0:
            raise ValueError('Must be a positive value')

        self.set_pair(id, self.get_pair(id) + value)

    def decrement_pair(self, id, value):
        if value < 0:
            raise ValueError('Must be a positive value')

        self.set_pair(id, self.get_pair(id) - value)
