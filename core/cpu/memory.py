class InvalidMemoryAddressError(Exception):
    pass

class Memory:
    def __init__(self):
        self._buffer = bytearray(0xffff)

    def read(self, address):
        if address < 0x0 or address > 0xffff:
            msg = 'Memory read out of bounds: ${0:06x}'.format(address)
            raise InvalidMemoryAddressError(msg)

        return self._buffer[address]

    def write(self, address, value):
        if address < 0x0 or address > 0xffff:
            msg = 'Memory write out of bounds: ${0:06x}'.format(address)
            raise InvalidMemoryAddressError(msg)

        self._buffer[address] = value
