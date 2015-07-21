
def get_bit(value, index):
    return (0 != (value & (1 << index)))

def zero_bit(value):
    return bool(value)

def sign_bit(value):
    return get_bit(value, 7)

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
