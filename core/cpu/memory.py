class InvalidMemoryAddressError(Exception):
    pass

class Memory:
    def __init__(self):
        self._buffer = bytearray(0xffff)

    def read_byte(self, address):
        if address < 0x0 or address > 0xffff:
            msg = 'Memory read out of bounds: ${0:06x}'.format(address)
            raise InvalidMemoryAddressError(msg)

        return self._buffer[address]

    def write_byte(self, address, value):
        if address < 0x0 or address > 0xffff:
            msg = 'Memory write out of bounds: ${0:06x}'.format(address)
            raise InvalidMemoryAddressError(msg)

        self._buffer[address] = value

    def read_double_byte(self, address):
        if address < 0x0 or address > 0xffff:
            msg = 'Memory read out of bounds: ${0:06x}'.format(address)
            raise InvalidMemoryAddressError(msg)

        end = address + 2
        return int.from_bytes(self._buffer[address:end], byteorder='little', 
            signed=False)

    def write_double_byte(self, address, value):
        if address < 0x0 or address > 0xffff:
            msg = 'Memory write out of bounds: ${0:06x}'.format(address)
            raise InvalidMemoryAddressError(msg)

        self._buffer[address - 1] = value >> 8
        self._buffer[address - 2] = value & 0xff

