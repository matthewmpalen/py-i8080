class UnhandledInstructionError(Exception):
    pass

class Instruction(object):
    def __init__(self, cpu):
        self._cpu = cpu

    def __call__(self):
        pass

class ACIInstruction(Instruction):
    def __call__(self):
        return 2

class ADDInstruction(Instruction):
    def __call__(self):
        return 1

class ADCInstruction(Instruction):
    def __call__(self):
        return 1

class ADIInstruction(Instruction):
    def __call__(self):
        return 2

class ANAInstruction(Instruction):
    def __call__(self):
        return 1

class ANIInstruction(Instruction):
    def __call__(self):
        return 2

class CALLInstruction(Instruction):
    def __call__(self):
        return 3

class CCInstruction(Instruction):
    def __call__(self):
        return 3

class CMInstruction(Instruction):
    def __call__(self):
        return 3

class CMAInstruction(Instruction):
    def __call__(self):
        return 1

class CMCInstruction(Instruction):
    def __call__(self):
        return 1

class CMPInstruction(Instruction):
    def __call__(self):
        return 1

class CNCInstruction(Instruction):
    def __call__(self):
        return 3

class CNZInstruction(Instruction):
    def __call__(self):
        return 3

class CPInstruction(Instruction):
    def __call__(self):
        return 3

class CPEInstruction(Instruction):
    def __call__(self):
        return 3

class CPIInstruction(Instruction):
    def __call__(self):
        return 2

class CPOInstruction(Instruction):
    def __call__(self):
        return 3

class CZInstruction(Instruction):
    def __call__(self):
        return 3

class DAAInstruction(Instruction):
    def __call__(self):
        return 1

class DADInstruction(Instruction):
    def __call__(self):
        return 1

class DCRInstruction(Instruction):
    def __call__(self):
        return 1

class DCXInstruction(Instruction):
    def __call__(self):
        return 1

class DIInstruction(Instruction):
    def __call__(self):
        return 1

class EIInstruction(Instruction):
    def __call__(self):
        return 1

class HLTInstruction(Instruction):
    def __call__(self):
        return 1

class INInstruction(Instruction):
    def __call__(self):
        return 2

class INRInstruction(Instruction):
    def __call__(self):
        return 1

class INXInstruction(Instruction):
    def __call__(self):
        return 1

class JCInstruction(Instruction):
    def __call__(self):
        return 3

class JMInstruction(Instruction):
    def __call__(self):
        return 3

class JMPInstruction(Instruction):
    def __call__(self):
        return 3

class JNCInstruction(Instruction):
    def __call__(self):
        return 3

class JNZInstruction(Instruction):
    def __call__(self):
        return 3

class JPInstruction(Instruction):
    def __call__(self):
        return 3

class JPEInstruction(Instruction):
    def __call__(self):
        return 3

class JPOInstruction(Instruction):
    def __call__(self):
        return 3

class JZInstruction(Instruction):
    def __call__(self):
        return 3

class LDAInstruction(Instruction):
    def __call__(self):
        return 3

class LDAXInstruction(Instruction):
    def __call__(self):
        return 1

class LHLDInstruction(Instruction):
    def __call__(self):
        return 3

class LXIInstruction(Instruction):
    def __call__(self):
        return 3

class MOVInstruction(Instruction):
    def __call__(self):
        return 1

class MVIInstruction(Instruction):
    def __call__(self):
        return 2

class NOPInstruction(Instruction):
    def __call__(self):
        return 1

class ORAInstruction(Instruction):
    def __call__(self):
        return 1

class ORIInstruction(Instruction):
    def __call__(self):
        return 2

class OUTInstruction(Instruction):
    def __call__(self):
        return 2

class PCHLInstruction(Instruction):
    def __call__(self):
        return 1

class POPInstruction(Instruction):
    def __call__(self):
        return 1

class PUSHInstruction(Instruction):
    def __call__(self):
        return 1

class RALInstruction(Instruction):
    def __call__(self):
        return 1

class RARInstruction(Instruction):
    def __call__(self):
        return 1

class RCInstruction(Instruction):
    def __call__(self):
        return 1

class RETInstruction(Instruction):
    def __call__(self):
        return 1

class RLCInstruction(Instruction):
    def __call__(self):
        return 1

class RMInstruction(Instruction):
    def __call__(self):
        return 1

class RNCInstruction(Instruction):
    def __call__(self):
        return 1

class RNZInstruction(Instruction):
    def __call__(self):
        return 1

class RPInstruction(Instruction):
    def __call__(self):
        return 1

class RPEInstruction(Instruction):
    def __call__(self):
        return 1

class RPOInstruction(Instruction):
    def __call__(self):
        return 1

class RRCInstruction(Instruction):
    def __call__(self):
        return 1

class RSTInstruction(Instruction):
    def __call__(self):
        return 1

class RZInstruction(Instruction):
    def __call__(self):
        return 1

class SBBInstruction(Instruction):
    def __call__(self):
        return 1

class SBIInstruction(Instruction):
    def __call__(self):
        return 2

class SHLDInstruction(Instruction):
    def __call__(self):
        return 3

class SPHLInstruction(Instruction):
    def __call__(self):
        return 1

class STAInstruction(Instruction):
    def __call__(self):
        return 3

class STAXInstruction(Instruction):
    def __call__(self):
        return 1

class STCInstruction(Instruction):
    def __call__(self):
        return 1

class SUBInstruction(Instruction):
    def __call__(self):
        return 1

class SUIInstruction(Instruction):
    def __call__(self):
        return 2

class XCHGInstruction(Instruction):
    def __call__(self):
        return 1

class XRAInstruction(Instruction):
    def __call__(self):
        return 1

class XRIInstruction(Instruction):
    def __call__(self):
        return 2

class XTHLInstruction(Instruction):
    def __call__(self):
        return 1
