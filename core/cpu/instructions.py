class UnhandledInstructionError(Exception):
    pass

class Instruction(object):
    def __init__(self, cpu):
        self._cpu = cpu

    def __call__(self):
        pass

class NOPInstruction(Instruction):
    def __call__(self):
        return 1

class LXIInstruction(Instruction):
    def __call__(self):
        return 3

class STAXInstruction(Instruction):
    def __call__(self):
        return 1

class INXInstruction(Instruction):
    def __call__(self):
        return 1

class INRInstruction(Instruction):
    def __call__(self):
        return 1

class DCRInstruction(Instruction):
    def __call__(self):
        return 1

class MVIInstruction(Instruction):
    def __call__(self):
        return 2

class RLCInstruction(Instruction):
    def __call__(self):
        return 1

class DADInstruction(Instruction):
    def __call__(self):
        return 1

class LDAXInstruction(Instruction):
    def __call__(self):
        return 1

class DCXInstruction(Instruction):
    def __call__(self):
        return 1

class RRCInstruction(Instruction):
    def __call__(self):
        return 1
