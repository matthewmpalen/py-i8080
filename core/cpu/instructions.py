# Python
import logging

# External
from numpy import int16, uint16

# Local
from .registers import RegID, DRegID

class UnhandledInstructionError(Exception):
    pass

class Instruction(object):
    logger = logging.getLogger('Instruction')

    def __init__(self, cpu):
        self._cpu = cpu
        self._size = 1

    def __call__(self):
        Instruction.logger.info(self)
        self._cpu.increment_program_counter(self._size)

    def __str__(self):
        return 'Instruction'

class ACIInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(ACIInstruction, self).__init__(*args, **kwargs)
        self._size = 2
        self._immediate = self._cpu.get_next_byte()
    
    def __call__(self, *args, **kwargs):
        flags = self._cpu.registers.increment(
            RegID.A, 
            (self._immediate + self._cpu.condition_flags.cy)
        )

        self._cpu.condition_flags.s = flags['s']
        self._cpu.condition_flags.z = flags['z']
        self._cpu.condition_flags.cy = flags['cy']
        self._cpu.condition_flags.p = flags['p']
       
        super(ACIInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'ACI'

class ADDInstruction(Instruction):
    def __init__(self, cpu, register):
        super(ADDInstruction, self).__init__(cpu)

        if register != DRegID.M:
            self._addend = self._cpu.registers.get(register)
        else:
            address = self._cpu.registers.get_pair(DRegID.HL)
            self._addend = self._cpu.ram.read(address)
    
    def __call__(self, *args, **kwargs):
        flags = self._cpu.registers.increment(
            RegID.A, 
            self._addend
        )

        self._cpu.condition_flags.s = flags['s']
        self._cpu.condition_flags.z = flags['z']
        self._cpu.condition_flags.cy = flags['cy']
        self._cpu.condition_flags.p = flags['p']

        super(ADDInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'ADD'

class ADCInstruction(Instruction):
    def __init__(self, cpu, register):
        super(ADCInstruction, self).__init__(cpu)

        if register != 'm':
            self._addend = self._cpu.registers.get(register)
        else:
            address = self._cpu.registers.get_pair(DRegID.HL)
            self._addend = self._cpu.ram.read(address)

    def __call__(self, *args, **kwargs):
        flags = self._cpu.registers.increment(
            RegID.A, 
            (self._addend + self._cpu.condition_flags.cy)
        )

        self._cpu.condition_flags.s = flags['s']
        self._cpu.condition_flags.z = flags['z']
        self._cpu.condition_flags.cy = flags['cy']
        self._cpu.condition_flags.p = flags['p']

        super(ADCInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'ADC'

class ADIInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(ADIInstruction, self).__init__(*args, **kwargs)
        self._size = 2
        self._immediate = self._cpu.get_next_byte()
    
    def __call__(self, *args, **kwargs):
        flags = self._cpu.registers.increment(
            RegID.A, 
            self._immediate
        )

        self._cpu.condition_flags.s = flags['s']
        self._cpu.condition_flags.z = flags['z']
        self._cpu.condition_flags.cy = flags['cy']
        self._cpu.condition_flags.p = flags['p']
       
        super(ADIInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'ADI'

class ANAInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(ANAInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'ANA'

class ANIInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(ANIInstruction, self).__init__(*args, **kwargs)
        self._size = 2

    def __call__(self, *args, **kwargs):
        super(ANIInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'ANI'

class CALLInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(CALLInstruction, self).__init__(*args, **kwargs)
        self._size = 3

    def __call__(self, *args, **kwargs):
        super(CALLInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'CALL'

class CCInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(CCInstruction, self).__init__(*args, **kwargs)
        self._size = 3

    def __call__(self, *args, **kwargs):
        super(CCInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'CC'

class CMInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(CMInstruction, self).__init__(*args, **kwargs)
        self._size = 3

    def __call__(self, *args, **kwargs):
        super(CMInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'CM'

class CMAInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(CMAInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'CMA'

class CMCInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(CMCInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'CMC'

class CMPInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(CMPInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'CMP'

class CNCInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(CNCInstruction, self).__init__(*args, **kwargs)
        self._size = 3
    
    def __call__(self, *args, **kwargs):
        super(CNCInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'CNC'

class CNZInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(CNZInstruction, self).__init__(*args, **kwargs)
        self._size = 3
    
    def __call__(self, *args, **kwargs):
        super(CNZInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'CNZ'

class CPInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(CPInstruction, self).__init__(*args, **kwargs)
        self._size = 3
    
    def __call__(self, *args, **kwargs):
        super(CPInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'CP'

class CPEInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(CPEInstruction, self).__init__(*args, **kwargs)
        self._size = 3
    
    def __call__(self, *args, **kwargs):
        super(CPEInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'CPE'

class CPIInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(CPIInstruction, self).__init__(*args, **kwargs)
        self._size = 2
 
    def __call__(self, *args, **kwargs):
        super(CPIInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'CPI'

class CPOInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(CPOInstruction, self).__init__(*args, **kwargs)
        self._size = 3
    
    def __call__(self, *args, **kwargs):
        super(CPOInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'CPO'

class CZInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(CZInstruction, self).__init__(*args, **kwargs)
        self._size = 3
 
    def __call__(self, *args, **kwargs):
        super(CZInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'CZ'

class DAAInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(DAAInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'DAA'

class DADInstruction(Instruction):
    def __init__(self, cpu, register_pair):
        super(DADInstruction, self).__init__(cpu)
        self._register_pair = register_pair

    def __call__(self, *args, **kwargs):
        if self._register_pair == DRegID.SP:
            flags = self._cpu.registers.increment_pair(
                DRegID.HL, 
                self._cpu.get_stack_pointer()
            )
        else:
            flags = self._cpu.registers.increment_pair(
                DRegID.HL, 
                self._cpu.registers.get_pair(self._register_pair)
            )

        self._cpu.condition_flags.cy = flags['cy']

        super(DADInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'DAD'

class DCRInstruction(Instruction):
    def __init__(self, cpu, register):
        super(DCRInstruction, self).__init__(cpu)
        self._register = register

    def __call__(self, *args, **kwargs):
        if self._register != DRegID.M:
            flags = self._cpu.registers.decrement(self._register, 1)
        else:
            flags = self._cpu.registers.decrement_pair(DRegID.HL, 1)

        self._cpu.condition_flags.s = flags['s']
        self._cpu.condition_flags.z = flags['z']
        self._cpu.condition_flags.p = flags['p']

        super(DCRInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'DCR'

class DCXInstruction(Instruction):
    def __init__(self, cpu, register_pair):
        super(DCXInstruction, self).__init__(cpu)
        self._register_pair = register_pair

    def __call__(self, *args, **kwargs):
        if self._register_pair == DRegID.SP:
            self._cpu.decrement_stack_pointer(1)
        else:
            self._cpu.registers.decrement_pair(self._register_pair, 1)

        super(DCXInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'DCX'

class DIInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(DIInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'DI'

class EIInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(EIInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'EI'

class HLTInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(HLTInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'HLT'

class INInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(INInstruction, self).__init__(*args, **kwargs)
        self._size = 2
    
    def __call__(self, *args, **kwargs):
        super(INInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'IN'

class INRInstruction(Instruction):
    def __init__(self, cpu, register):
        super(INRInstruction, self).__init__(cpu)
        self._register = register

    def __call__(self, *args, **kwargs):
        if self._register != DRegID.M:
            flags = self._cpu.registers.increment(self._register, 1)
        else:
            flags = self._cpu.registers.increment_pair(DRegID.HL, 1)

        self._cpu.condition_flags.s = flags['s']
        self._cpu.condition_flags.z = flags['z']
        self._cpu.condition_flags.p = flags['p']

        super(INRInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'INR'

class INXInstruction(Instruction):
    def __init__(self, cpu, register_pair):
        super(INXInstruction, self).__init__(cpu)
        self._register_pair = register_pair

    def __call__(self, *args, **kwargs):
        if self._register_pair == DRegID.SP:
            self._cpu.increment_stack_pointer(1)
        else:
            self._cpu.registers.increment_pair(self._register_pair, 1)

        super(INXInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'INX'

class JCInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(JCInstruction, self).__init__(*args, **kwargs)
        self._size = 3

    def __call__(self, *args, **kwargs):
        super(JCInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'JC'

class JMInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(JMInstruction, self).__init__(*args, **kwargs)
        self._size = 3
    
    def __call__(self, *args, **kwargs):
        super(JMInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'JM'

class JMPInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(JMPInstruction, self).__init__(*args, **kwargs)
        self._size = 3
    
    def __call__(self, *args, **kwargs):
        super(JMPInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'JMP'

class JNCInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(JNCInstruction, self).__init__(*args, **kwargs)
        self._size = 3
 
    def __call__(self, *args, **kwargs):
        super(JNCInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'JNC'

class JNZInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(JNZInstruction, self).__init__(*args, **kwargs)
        self._size = 3

    def __call__(self, *args, **kwargs):
        super(JNZInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'JNZ'

class JPInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(JPInstruction, self).__init__(*args, **kwargs)
        self._size = 3
 
    def __call__(self, *args, **kwargs):
        super(JPInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'JP'

class JPEInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(JPEInstruction, self).__init__(*args, **kwargs)
        self._size = 3
 
    def __call__(self, *args, **kwargs):
        super(JPEInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'JPE'

class JPOInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(JPOInstruction, self).__init__(*args, **kwargs)
        self._size = 3

    def __call__(self, *args, **kwargs):
        super(JPOInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'JPO'

class JZInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(JZInstruction, self).__init__(*args, **kwargs)
        self._size = 3
 
    def __call__(self, *args, **kwargs):
        super(JZInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'JZ'

class LDAInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(LDAInstruction, self).__init__(*args, **kwargs)
        self._size = 3
 
    def __call__(self, *args, **kwargs):
        super(LDAInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'LDA'

class LDAXInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(LDAXInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'LDAX'

class LHLDInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(LHLDInstruction, self).__init__(*args, **kwargs)
        self._size = 3
 
    def __call__(self, *args, **kwargs):
        super(LHLDInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'LHLD'

class LXIInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(LXIInstruction, self).__init__(*args, **kwargs)
        self._size = 3
    
    def __call__(self, *args, **kwargs):
        super(LXIInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'LXI'

class MOVInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(MOVInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'MOV'

class MVIInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(MVIInstruction, self).__init__(*args, **kwargs)
        self._size = 2

    def __call__(self, *args, **kwargs):
        super(MVIInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'MVI'

class NOPInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(NOPInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'NOP'

class ORAInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(ORAInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'ORA'

class ORIInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(ORIInstruction, self).__init__(*args, **kwargs)
        self._size = 2

    def __call__(self, *args, **kwargs):
        super(ORIInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'ORI'

class OUTInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(OUTInstruction, self).__init__(*args, **kwargs)
        self._size = 2
   
    def __call__(self, *args, **kwargs):
        super(OUTInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'OUT'

class PCHLInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(PCHLInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'PCHL'

class POPInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(POPInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'POP'

class PUSHInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(PUSHInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'PUSH'

class RALInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(RALInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'RAL'

class RARInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(RARInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'RAR'

class RCInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(RCInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'RC'

class RETInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(RETInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'RET'

class RLCInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(RLCInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'RLC'

class RMInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(RMInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'RM'

class RNCInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(RNCInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'RNC'

class RNZInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(RNZInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'RNZ'

class RPInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(RPInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'RP'

class RPEInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(RPEInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'RPE'

class RPOInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(RPOInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'RPO'

class RRCInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(RRCInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'RRC'

class RSTInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(RSTInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'RST'

class RZInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(RZInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'RZ'

class SBBInstruction(Instruction):
    def __init__(self, cpu, register):
        super(SBBInstruction, self).__init__(cpu)

        if register != DRegID.M:
            self._subtrahend = self._cpu.registers.get(register)
        else:
            address = self._cpu.registers.get_pair(DRegID.HL)
            self._subtrahend = self._cpu.ram.read(address)
 
    def __call__(self, *args, **kwargs):
        flags = self._cpu.registers.decrement(
            RegID.A, 
            (self._subtrahend + self._cpu.condition_flags.cy)
        )

        self._cpu.condition_flags.s = flags['s']
        self._cpu.condition_flags.z = flags['z']
        self._cpu.condition_flags.cy = flags['cy']
        self._cpu.condition_flags.p = flags['p']
 
        super(SBBInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'SBB'

class SBIInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(SBIInstruction, self).__init__(*args, **kwargs)
        self._size = 2
    
    def __call__(self, *args, **kwargs):
        immediate = self._cpu.get_next_byte()
        answer = (
            self._cpu.registers.get(RegID.A) - 
            immediate - 
            self._cpu.condition_flags.cy
        )

        flags = self._cpu.registers.decrement(
            RegID.A, 
            (immediate + self._cpu.condition_flags.cy)
        )

        self._cpu.condition_flags.s = flags['s']
        self._cpu.condition_flags.z = flags['z']
        self._cpu.condition_flags.cy = flags['cy']
        self._cpu.condition_flags.p = flags['p']

        super(SBIInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'SBI'

class SHLDInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(SHLDInstruction, self).__init__(*args, **kwargs)
        self._size = 3
    
    def __call__(self, *args, **kwargs):
        super(SHLDInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'SHLD'

class SPHLInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(SPHLInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'SPHL'

class STAInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(STAInstruction, self).__init__(*args, **kwargs)
        self._size = 3

    def __call__(self, *args, **kwargs):
        super(STAInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'STA'

class STAXInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(STAXInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'STAX'

class STCInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(STCInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'STC'

class SUBInstruction(Instruction):
    def __init__(self, cpu, register):
        super(SUBInstruction, self).__init__(cpu)

        if register != DRegID.M:
            self._subtrahend = self._cpu.registers.get(register)
        else:
            address = self._cpu.registers.get_pair(DRegID.HL)
            self._subtrahend = self._cpu.ram.read(address)
 
    def __call__(self, *args, **kwargs):
        flags = self._cpu.registers.decrement(
            RegID.A, 
            self._subtrahend
        )

        self._cpu.condition_flags.s = flags['s']
        self._cpu.condition_flags.z = flags['z']
        self._cpu.condition_flags.cy = flags['cy']
        self._cpu.condition_flags.p = flags['p']

        super(SUBInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'SUB'

class SUIInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(SUIInstruction, self).__init__(*args, **kwargs)
        self._size = 2
        self._immediate = self._cpu.get_next_byte()
    
    def __call__(self, *args, **kwargs):
        flags = self._cpu.registers.decrement(
            RegID.A, 
            self._immediate
        )

        self._cpu.condition_flags.s = flags['s']
        self._cpu.condition_flags.z = flags['z']
        self._cpu.condition_flags.cy = flags['cy']
        self._cpu.condition_flags.p = flags['p']

        super(SUIInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'SUI'

class XCHGInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(XCHGInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'XCHG'

class XRAInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(XRAInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'XRA'

class XRIInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(XRIInstruction, self).__init__(*args, **kwargs)
        self._size = 2

    def __call__(self, *args, **kwargs):
        super(XRIInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'XRI'

class XTHLInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(XTHLInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'XTHL'
