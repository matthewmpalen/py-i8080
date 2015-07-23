def get_bit(value, index):
    return value & (1 << index)

def zero_bit(value):
    return not bool(value)

def sign_bit(value):
    return (0 != get_bit(value, 7))

def carry_bit(value):
    return value < 0x00 or value > 0xff

def parity_bit(value):
    return (bin(value).count('1') % 2) == 0

class ConditionFlags(object):
    def __init__(self):
        self.s = False
        self.z = False
        self.p = False
        self.cy = False
        self.ac = False
        self.pad = False
