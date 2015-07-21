# Python
import logging

from enum import IntEnum, unique

from .flags import zero_bit, sign_bit, carry_bit, parity_bit

@unique
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

def flags(value):
    return {
        'z': zero_bit(value), 
        's': sign_bit(value), 
        'cy': carry_bit(value), 
        'p': parity_bit(value)
    }

class Registers(object):
    logger = logging.getLogger('Registers')

    def __init__(self):
        self._items = bytearray(7)

    def get(self, id):
        return self._items[id]

    def set(self, id, value):
        self._items[id] = value & 0xff

    def increment(self, id, value):
        if value < 0:
            raise ValueError('Must be a positive value')

        answer = self._items[id] + value
        Registers.logger.info(
            'increment {0}: {1:x} + {2:x} = {3:x}'.format(
                id.name, self._items[id], value, answer
            )
        )

        self.set(id, answer)

        return flags(answer)

    def decrement(self, id, value):
        if value < 0:
            raise ValueError('Must be a positive value')

        answer = self._items[id] - value
        Registers.logger.info(
            'decrement {0}: {1:x} - {2:x} = {3:x}'.format(
                id.name, self._items[id], value, answer
            )
        )

        self.set(id, answer)

        return flags(answer)

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

        answer = self.get_pair(id) + value
        Registers.logger.info(
            'increment_pair {0}: {1:x} + {2:x} = {3:x}'.format(
                id.name, self.get_pair(id), value, answer
            )
        )

        self.set_pair(id, answer)

        return flags(answer)

    def decrement_pair(self, id, value):
        if value < 0:
            raise ValueError('Must be a positive value')

        answer = self.get_pair(id) - value
        Registers.logger.info(
            'decrement_pair {0}: {1:x} - {2:x} = {3:x}'.format(
                id.name, self.get_pair(id), value, answer
            )
        )

        self.set_pair(id, answer)
        
        return flags(answer)
