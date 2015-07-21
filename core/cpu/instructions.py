from numpy import int16, uint16

from .registers import RegID, DRegID

def get_bit(value, index):
    return (0 != (value & (1 << index)))

def sign_bit(value):
    return get_bit(value, 7)

def parity_bit(value):
    return (bin(value).count('1') % 2) == 0

class UnhandledInstructionError(Exception):
    pass

class Instruction(object):
    def __init__(self, cpu):
        self._cpu = cpu
        self._size = 1

    def __call__(self):
        self._cpu.program_counter += self._size

class ACIInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(ACIInstruction, self).__init__(*args, **kwargs)
        self._size = 2
    
    def __call__(self, *args, **kwargs):
        immediate = self._cpu.getNextByte()
        answer = (
            self._cpu.registers.get(RegID.A) + 
            immediate + 
            self._cpu.condition_flags.cy
        )

        self._cpu.condition_flags.z = bool(answer)
        self._cpu.condition_flags.s = sign_bit(answer)
        self._cpu.condition_flags.cy = answer > 0xff
        self._cpu.p = parity_bit(answer)
        self._cpu.registers.set(RegID.A, answer)
       
        super(ACIInstruction, self).__call__(*args, **kwargs)

class ADDInstruction(Instruction):
    def __init__(self, cpu, register):
        super(ADDInstruction, self).__init__(cpu)

        if register != DRegID.M:
            self._addend = self._cpu.registers.get(register)
        else:
            address = self._cpu.registers.get_pair(DRegID.HL)
            self._addend = self._cpu.ram.read(address)
    
    def __call__(self, *args, **kwargs):
        answer = self._cpu.registers.get(RegID.A) + self._addend

        self._cpu.condition_flags.z = bool(answer)
        self._cpu.condition_flags.s = sign_bit(answer)
        self._cpu.condition_flags.cy = answer > 0xff
        self._cpu.p = parity_bit(answer)
        self._cpu.registers.set(RegID.A, answer)

        super(ADDInstruction, self).__call__(*args, **kwargs)

class ADCInstruction(Instruction):
    def __init__(self, cpu, register):
        super(ADCInstruction, self).__init__(cpu)

        if register != 'm':
            self._addend = self._cpu.registers.get(register)
        else:
            address = self._cpu.registers.get_pair(DRegID.HL)
            self._addend = self._cpu.ram.read(address)

    def __call__(self, *args, **kwargs):
        answer = (
            self._cpu.registers.get(RegID.A) + 
            self._addend + 
            self._cpu.condition_flags.cy
        )

        self._cpu.condition_flags.z = bool(answer)
        self._cpu.condition_flags.s = sign_bit(answer)
        self._cpu.condition_flags.cy = answer > 0xff
        self._cpu.p = parity_bit(answer)
        self._cpu.registers.set(RegID.A, answer)

        super(ADCInstruction, self).__call__(*args, **kwargs)

class ADIInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(ADIInstruction, self).__init__(*args, **kwargs)
        self._size = 2
    
    def __call__(self, *args, **kwargs):
        immediate = self._cpu.getNextByte()
        answer = self._cpu.registers.get(RegID.A) + immediate

        self._cpu.condition_flags.z = bool(answer)
        self._cpu.condition_flags.s = sign_bit(answer)
        self._cpu.condition_flags.cy = answer > 0xff
        self._cpu.p = parity_bit(answer)
        self._cpu.registers.set(RegID.A, answer)
       
        super(ADIInstruction, self).__call__(*args, **kwargs)

class ANAInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(ANAInstruction, self).__call__(*args, **kwargs)

class ANIInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(ANIInstruction, self).__init__(*args, **kwargs)
        self._size = 2

    def __call__(self, *args, **kwargs):
        super(ANIInstruction, self).__call__(*args, **kwargs)

class CALLInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(CALLInstruction, self).__init__(*args, **kwargs)
        self._size = 3

    def __call__(self, *args, **kwargs):
        super(CALLInstruction, self).__call__(*args, **kwargs)

class CCInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(CCInstruction, self).__init__(*args, **kwargs)
        self._size = 3

    def __call__(self, *args, **kwargs):
        super(CCInstruction, self).__call__(*args, **kwargs)

class CMInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(CMInstruction, self).__init__(*args, **kwargs)
        self._size = 3

    def __call__(self, *args, **kwargs):
        super(CMInstruction, self).__call__(*args, **kwargs)

class CMAInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(CMAInstruction, self).__call__(*args, **kwargs)

class CMCInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(CMCInstruction, self).__call__(*args, **kwargs)

class CMPInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(CMPInstruction, self).__call__(*args, **kwargs)

class CNCInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(CNCInstruction, self).__init__(*args, **kwargs)
        self._size = 3
    
    def __call__(self, *args, **kwargs):
        super(CNCInstruction, self).__call__(*args, **kwargs)

class CNZInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(CNZInstruction, self).__init__(*args, **kwargs)
        self._size = 3
    
    def __call__(self, *args, **kwargs):
        super(CNZInstruction, self).__call__(*args, **kwargs)

class CPInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(CPInstruction, self).__init__(*args, **kwargs)
        self._size = 3
    
    def __call__(self, *args, **kwargs):
        super(CPInstruction, self).__call__(*args, **kwargs)

class CPEInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(CPEInstruction, self).__init__(*args, **kwargs)
        self._size = 3
    
    def __call__(self, *args, **kwargs):
        super(CPEInstruction, self).__call__(*args, **kwargs)

class CPIInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(CPIInstruction, self).__init__(*args, **kwargs)
        self._size = 2
 
    def __call__(self, *args, **kwargs):
        super(CPIInstruction, self).__call__(*args, **kwargs)

class CPOInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(CPOInstruction, self).__init__(*args, **kwargs)
        self._size = 3
    
    def __call__(self, *args, **kwargs):
        super(CPOInstruction, self).__call__(*args, **kwargs)

class CZInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(CZInstruction, self).__init__(*args, **kwargs)
        self._size = 3
 
    def __call__(self, *args, **kwargs):
        super(CZInstruction, self).__call__(*args, **kwargs)

class DAAInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(DAAInstruction, self).__call__(*args, **kwargs)

class DADInstruction(Instruction):
    def __init__(self, cpu, register_pair):
        super(DADInstruction, self).__init__(cpu)
        self._register_pair = register_pair

    def __call__(self, *args, **kwargs):
        if self._register_pair == DRegID.SP:
            self._cpu.registers.increment_pair(
                DRegID.HL, 
                self._cpu.stack_pointer
            )
        else:
            self._cpu.registers.increment_pair(
                DRegID.HL, 
                self._cpu.registers.get_pair(self._register_pair)
            )

        self._cpu.condition_flags.cy = (
            self._cpu.registers.get_pair(DRegID.HL) > 0xff
        )

        super(DADInstruction, self).__call__(*args, **kwargs)

class DCRInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(DCRInstruction, self).__call__(*args, **kwargs)

class DCXInstruction(Instruction):
    def __init__(self, cpu, register_pair):
        super(DCXInstruction, self).__init__(cpu)
        self._register_pair = register_pair

    def __call__(self, *args, **kwargs):
        if self._register_pair == DRegID.SP:
            self._cpu.sp -= 1
        else:
            self._cpu.registers.decrement_pair(self._register_pair, 1)

        super(DCXInstruction, self).__call__(*args, **kwargs)

class DIInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(DIInstruction, self).__call__(*args, **kwargs)

class EIInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(EIInstruction, self).__call__(*args, **kwargs)

class HLTInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(HLTInstruction, self).__call__(*args, **kwargs)

class INInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(INInstruction, self).__init__(*args, **kwargs)
        self._size = 2
    
    def __call__(self, *args, **kwargs):
        super(INInstruction, self).__call__(*args, **kwargs)

class INRInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(INRInstruction, self).__call__(*args, **kwargs)

class INXInstruction(Instruction):
    def __init__(self, cpu, register_pair):
        super(INXInstruction, self).__init__(cpu)
        self._register_pair = register_pair

    def __call__(self, *args, **kwargs):
        if self._register_pair == DRegID.SP:
            self._cpu.stack_pointer += 1
        else:
            self._cpu.registers.increment_pair(self._register_pair, 1)

        super(INXInstruction, self).__call__(*args, **kwargs)

class JCInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(JCInstruction, self).__init__(*args, **kwargs)
        self._size = 3

    def __call__(self, *args, **kwargs):
        super(JCInstruction, self).__call__(*args, **kwargs)

class JMInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(JMInstruction, self).__init__(*args, **kwargs)
        self._size = 3
    
    def __call__(self, *args, **kwargs):
        super(JMInstruction, self).__call__(*args, **kwargs)

class JMPInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(JMPInstruction, self).__init__(*args, **kwargs)
        self._size = 3
    
    def __call__(self, *args, **kwargs):
        super(JMPInstruction, self).__call__(*args, **kwargs)

class JNCInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(JNCInstruction, self).__init__(*args, **kwargs)
        self._size = 3
 
    def __call__(self, *args, **kwargs):
        super(JNCInstruction, self).__call__(*args, **kwargs)

class JNZInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(JNZInstruction, self).__init__(*args, **kwargs)
        self._size = 3

    def __call__(self, *args, **kwargs):
        super(JNZInstruction, self).__call__(*args, **kwargs)

class JPInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(JPInstruction, self).__init__(*args, **kwargs)
        self._size = 3
 
    def __call__(self, *args, **kwargs):
        super(JPInstruction, self).__call__(*args, **kwargs)

class JPEInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(JPEInstruction, self).__init__(*args, **kwargs)
        self._size = 3
 
    def __call__(self, *args, **kwargs):
        super(JPEInstruction, self).__call__(*args, **kwargs)

class JPOInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(JPOInstruction, self).__init__(*args, **kwargs)
        self._size = 3

    def __call__(self, *args, **kwargs):
        super(JPOInstruction, self).__call__(*args, **kwargs)

class JZInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(JZInstruction, self).__init__(*args, **kwargs)
        self._size = 3
 
    def __call__(self, *args, **kwargs):
        super(JZInstruction, self).__call__(*args, **kwargs)

class LDAInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(LDAInstruction, self).__init__(*args, **kwargs)
        self._size = 3
 
    def __call__(self, *args, **kwargs):
        super(LDAInstruction, self).__call__(*args, **kwargs)

class LDAXInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(LDAXInstruction, self).__call__(*args, **kwargs)

class LHLDInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(LHLDInstruction, self).__init__(*args, **kwargs)
        self._size = 3
 
    def __call__(self, *args, **kwargs):
        super(LHLDInstruction, self).__call__(*args, **kwargs)

class LXIInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(LXIInstruction, self).__init__(*args, **kwargs)
        self._size = 3
    
    def __call__(self, *args, **kwargs):
        super(LXIInstruction, self).__call__(*args, **kwargs)

class MOVInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(MOVInstruction, self).__call__(*args, **kwargs)

class MVIInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(MVIInstruction, self).__init__(*args, **kwargs)
        self._size = 2

    def __call__(self, *args, **kwargs):
        super(MVIInstruction, self).__call__(*args, **kwargs)

class NOPInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(NOPInstruction, self).__call__(*args, **kwargs)

class ORAInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(ORAInstruction, self).__call__(*args, **kwargs)

class ORIInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(ORIInstruction, self).__init__(*args, **kwargs)
        self._size = 2

    def __call__(self, *args, **kwargs):
        super(ORIInstruction, self).__call__(*args, **kwargs)

class OUTInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(OUTInstruction, self).__init__(*args, **kwargs)
        self._size = 2
   
    def __call__(self, *args, **kwargs):
        super(OUTInstruction, self).__call__(*args, **kwargs)

class PCHLInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(PCHLInstruction, self).__call__(*args, **kwargs)

class POPInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(POPInstruction, self).__call__(*args, **kwargs)

class PUSHInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(PUSHInstruction, self).__call__(*args, **kwargs)

class RALInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(RALInstruction, self).__call__(*args, **kwargs)

class RARInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(RARInstruction, self).__call__(*args, **kwargs)

class RCInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(RCInstruction, self).__call__(*args, **kwargs)

class RETInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(RETInstruction, self).__call__(*args, **kwargs)

class RLCInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(RLCInstruction, self).__call__(*args, **kwargs)

class RMInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(RMInstruction, self).__call__(*args, **kwargs)

class RNCInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(RNCInstruction, self).__call__(*args, **kwargs)

class RNZInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(RNZInstruction, self).__call__(*args, **kwargs)

class RPInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(RPInstruction, self).__call__(*args, **kwargs)

class RPEInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(RPEInstruction, self).__call__(*args, **kwargs)

class RPOInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(RPOInstruction, self).__call__(*args, **kwargs)

class RRCInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(RRCInstruction, self).__call__(*args, **kwargs)

class RSTInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(RSTInstruction, self).__call__(*args, **kwargs)

class RZInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(RZInstruction, self).__call__(*args, **kwargs)

class SBBInstruction(Instruction):
    def __init__(self, cpu, register):
        super(SBBInstruction, self).__init__(cpu)

        if register != DRegID.M:
            self._subtrahend = self._cpu.registers.get(register)
        else:
            address = self._cpu.registers.get_pair(DRegID.HL)
            self._subtrahend = self._cpu.ram.read(address)
 
    def __call__(self, *args, **kwargs):
        answer = (
            self._cpu.registers.get(RegID.A) - 
            self._subtrahend - 
            self._cpu.condition_flags.cy
        )

        self._cpu.condition_flags.z = bool(answer)
        self._cpu.condition_flags.s = sign_bit(answer)
        self._cpu.condition_flags.cy = answer < 0x00
        self._cpu.p = parity_bit(answer)
        self._cpu.registers.set(RegID.A, answer)
 
        super(SBBInstruction, self).__call__(*args, **kwargs)

class SBIInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(SBIInstruction, self).__init__(*args, **kwargs)
        self._size = 2
    
    def __call__(self, *args, **kwargs):
        immediate = self._cpu.getNextByte()
        answer = (
            self._cpu.registers.get(RegID.A) - 
            immediate - 
            self._cpu.condition_flags.cy
        )

        self._cpu.condition_flags.z = bool(answer)
        self._cpu.condition_flags.s = sign_bit(answer)
        self._cpu.condition_flags.cy = answer < 0x00
        self._cpu.p = parity_bit(answer)
        self._cpu.registers.set(RegID.A, answer)

        super(SBIInstruction, self).__call__(*args, **kwargs)

class SHLDInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(SHLDInstruction, self).__init__(*args, **kwargs)
        self._size = 3
    
    def __call__(self, *args, **kwargs):
        super(SHLDInstruction, self).__call__(*args, **kwargs)

class SPHLInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(SPHLInstruction, self).__call__(*args, **kwargs)

class STAInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(STAInstruction, self).__init__(*args, **kwargs)
        self._size = 3

    def __call__(self, *args, **kwargs):
        super(STAInstruction, self).__call__(*args, **kwargs)

class STAXInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(STAXInstruction, self).__call__(*args, **kwargs)

class STCInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(STCInstruction, self).__call__(*args, **kwargs)

class SUBInstruction(Instruction):
    def __init__(self, cpu, register):
        super(SUBInstruction, self).__init__(cpu)

        if register != DRegID.M:
            self._subtrahend = self._cpu.registers.get(register)
        else:
            address = self._cpu.registers.get_pair(DRegID.HL)
            self._subtrahend = self._cpu.ram.read(address)
 
    def __call__(self, *args, **kwargs):
        answer = (
            self._cpu.registers.get(RegID.A) - 
            self._subtrahend
        )

        self._cpu.condition_flags.z = bool(answer)
        self._cpu.condition_flags.s = sign_bit(answer)
        self._cpu.condition_flags.cy = answer < 0x00
        self._cpu.p = parity_bit(answer)
        self._cpu.registers.set(RegID.A, answer)

        super(SUBInstruction, self).__call__(*args, **kwargs)

class SUIInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(SUIInstruction, self).__init__(*args, **kwargs)
        self._size = 2
    
    def __call__(self, *args, **kwargs):
        immediate = self._cpu.getNextByte()
        answer = self._cpu.registers.get(RegID.A) - immediate

        self._cpu.condition_flags.z = bool(answer)
        self._cpu.condition_flags.s = sign_bit(answer)
        self._cpu.condition_flags.cy = answer < 0x00
        self._cpu.p = parity_bit(answer)
        self._cpu.registers.set(RegID.A, answer)

        super(SUIInstruction, self).__call__(*args, **kwargs)

class XCHGInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(XCHGInstruction, self).__call__(*args, **kwargs)

class XRAInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(XRAInstruction, self).__call__(*args, **kwargs)

class XRIInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(XRIInstruction, self).__init__(*args, **kwargs)
        self._size = 2

    def __call__(self, *args, **kwargs):
        super(XRIInstruction, self).__call__(*args, **kwargs)

class XTHLInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(XTHLInstruction, self).__call__(*args, **kwargs)
