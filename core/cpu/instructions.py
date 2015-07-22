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
            
    def __call__(self, *args, **kwargs):
        immediate = self._cpu.get_next_byte()

        flags = self._cpu.registers.increment(
            RegID.A, 
            (immediate + self._cpu.condition_flags.cy)
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
        self._register = register
    
    def __call__(self, *args, **kwargs):
        if self._register != DRegID.M:
            addend = self._cpu.registers.get(self._register)
        else:
            address = self._cpu.registers.get_pair(DRegID.HL)
            addend = self._cpu.ram.read(address)

        flags = self._cpu.registers.increment(
            RegID.A, 
            addend
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
        self._register = register

    def __call__(self, *args, **kwargs):
        if register != 'm':
            addend = self._cpu.registers.get(register)
        else:
            address = self._cpu.registers.get_pair(DRegID.HL)
            addend = self._cpu.ram.read(address)

        flags = self._cpu.registers.increment(
            RegID.A, 
            (addend + self._cpu.condition_flags.cy)
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
            
    def __call__(self, *args, **kwargs):
        immediate = self._cpu.get_next_byte()

        flags = self._cpu.registers.increment(
            RegID.A, 
            immediate
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
        Instruction.logger.info(self)
        ret = self._cpu.get_program_counter() + self._size
        self._cpu.ram.write_double_byte(self._cpu.get_stack_pointer(), ret)
        self._cpu.decrement_stack_pointer(2)

        address = self._cpu.get_next_double_byte()
        self._cpu.set_program_counter(address)

    def __str__(self):
        return 'CALL'

class CCInstruction(CALLInstruction):
    def __call__(self, *args, **kwargs):
        if self._cpu.condition_flags.cy:
            super(CCInstruction, self).__call__(*args, **kwargs)
        else:
            super(CALLInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'CC'

class CMInstruction(CALLInstruction):
    def __call__(self, *args, **kwargs):
        if self._cpu.condition_flags.s:
            super(CMInstruction, self).__call__(*args, **kwargs)
        else:
            super(CALLInstruction, self).__call__(*args, **kwargs)

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

class CNCInstruction(CALLInstruction):
    def __call__(self, *args, **kwargs):
        if not self._cpu.condition_flags.cy:
            super(CNCInstruction, self).__call__(*args, **kwargs)
        else:
            super(CALLInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'CNC'

class CNZInstruction(CALLInstruction):
    def __call__(self, *args, **kwargs):
        if not self._cpu.condition_flags.z:
            super(CNZInstruction, self).__call__(*args, **kwargs)
        else:
            super(CALLInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'CNZ'

class CPInstruction(CALLInstruction):
    def __call__(self, *args, **kwargs):
        if not self._cpu.condition_flags.s:
            super(CPInstruction, self).__call__(*args, **kwargs)
        else:
            super(CALLInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'CP'

class CPEInstruction(CALLInstruction):
    def __call__(self, *args, **kwargs):
        if self._cpu.condition_flags.p:
            super(CPEInstruction, self).__call__(*args, **kwargs)
        else:
            super(CALLInstruction, self).__call__(*args, **kwargs)

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

class CPOInstruction(CALLInstruction):
    def __call__(self, *args, **kwargs):
        if not self._cpu.condition_flags.p:
            super(CPOInstruction, self).__call__(*args, **kwargs)
        else:
            super(CALLInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'CPO'

class CZInstruction(CALLInstruction):
    def __call__(self, *args, **kwargs):
        if self._cpu.condition_flags.z:
            super(CZInstruction, self).__call__(*args, **kwargs)
        else:
            super(CALLInstruction, self).__call__(*args, **kwargs)

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

class JMPInstruction(Instruction):
    def __init__(self, *args, **kwargs):
        super(JMPInstruction, self).__init__(*args, **kwargs)
        self._size = 3
    
    def __call__(self, *args, **kwargs):
        Instruction.logger.info(self)
        address = self._cpu.get_next_double_byte()
        self._cpu.set_program_counter(address)

    def __str__(self):
        return 'JMP'

class JCInstruction(JMPInstruction):
    def __call__(self, *args, **kwargs):
        if self._cpu.condition_flags.cy:
            super(JCInstruction, self).__call__(*args, **kwargs)
        else:
            super(JMPInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'JC'

class JMInstruction(JMPInstruction):
    def __call__(self, *args, **kwargs):
        if self._cpu.condition_flags.s:
            super(JMInstruction, self).__call__(*args, **kwargs)
        else:
            super(JMPInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'JM'

class JNCInstruction(JMPInstruction):
    def __call__(self, *args, **kwargs):
        if not self._cpu.condition_flags.cy:
            super(JNCInstruction, self).__call__(*args, **kwargs)
        else:
            super(JMPInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'JNC'

class JNZInstruction(JMPInstruction):
    def __call__(self, *args, **kwargs):
        if not self._cpu.condition_flags.z:
            super(JNZInstruction, self).__call__(*args, **kwargs)
        else:
            super(JMPInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'JNZ'

class JPInstruction(JMPInstruction):
    def __call__(self, *args, **kwargs):
        if not self._cpu.condition_flags.s:
            super(JPInstruction, self).__call__(*args, **kwargs)
        else:
            super(JMPInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'JP'

class JPEInstruction(JMPInstruction):
    def __call__(self, *args, **kwargs):
        if self._cpu.condition_flags.p:
            super(JPEInstruction, self).__call__(*args, **kwargs)
        else:
            super(JMPInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'JPE'

class JPOInstruction(JMPInstruction):
    def __call__(self, *args, **kwargs):
        if not self._cpu.condition_flags.p:
            super(JPOInstruction, self).__call__(*args, **kwargs)
        else:
            super(JMPInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'JPO'

class JZInstruction(JMPInstruction):
    def __call__(self, *args, **kwargs):
        if self._cpu.condition_flags.z:
            super(JZInstruction, self).__call__(*args, **kwargs)
        else:
            super(JMPInstruction, self).__call__(*args, **kwargs)

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
        Instruction.logger.info(self)
        address = self._cpu.get_pair(DRegID.HL)
        self._cpu.set_program_counter(address)

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

class RETInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        address = self._cpu.ram.read_double_byte(
            self._cpu.get_stack_pointer()
        ) 
        self._cpu.set_program_counter(address)
        self._cpu.increment_stack_pointer(2)

    def __str__(self):
        return 'RET'

class RCInstruction(RETInstruction):
    def __call__(self, *args, **kwargs):
        if self._cpu.condition_flags.cy:
            super(RCInstruction, self).__call__(*args, **kwargs)
        else:
            super(RETInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'RC'

class RLCInstruction(Instruction):
    def __call__(self, *args, **kwargs):
        super(RLCInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'RLC'

class RMInstruction(RETInstruction):
    def __call__(self, *args, **kwargs):
        if self._cpu.condition_flags.s:
            super(RMInstruction, self).__call__(*args, **kwargs)
        else:
            super(RETInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'RM'

class RNCInstruction(RETInstruction):
    def __call__(self, *args, **kwargs):
        if not self._cpu.condition_flags.cy:
            super(RNCInstruction, self).__call__(*args, **kwargs)
        else:
            super(RETInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'RNC'

class RNZInstruction(RETInstruction):
    def __call__(self, *args, **kwargs):
        if not self._cpu.condition_flags.z:
            super(RNZInstruction, self).__call__(*args, **kwargs)
        else:
            super(RETInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'RNZ'

class RPInstruction(RETInstruction):
    def __call__(self, *args, **kwargs):
        if not self._cpu.condition_flags.s:
            super(RPInstruction, self).__call__(*args, **kwargs)
        else:
            super(RETInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'RP'

class RPEInstruction(RETInstruction):
    def __call__(self, *args, **kwargs):
        if self._cpu.condition_flags.p:
            super(RPEInstruction, self).__call__(*args, **kwargs)
        else:
            super(RETInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'RPE'

class RPOInstruction(RETInstruction):
    def __call__(self, *args, **kwargs):
        if not self._cpu.condition_flags.p:
            super(RPOInstruction, self).__call__(*args, **kwargs)
        else:
            super(RETInstruction, self).__call__(*args, **kwargs)

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

class RZInstruction(RETInstruction):
    def __call__(self, *args, **kwargs):
        if self._cpu.condition_flags.z:
            super(RZInstruction, self).__call__(*args, **kwargs)
        else:
            super(RETInstruction, self).__call__(*args, **kwargs)

    def __str__(self):
        return 'RZ'

class SBBInstruction(Instruction):
    def __init__(self, cpu, register):
        super(SBBInstruction, self).__init__(cpu)
        self._register = register

    def __call__(self, *args, **kwargs):
        if self._register != DRegID.M:
            subtrahend = self._cpu.registers.get(self._register)
        else:
            address = self._cpu.registers.get_pair(DRegID.HL)
            subtrahend = self._cpu.ram.read(address)
 
        flags = self._cpu.registers.decrement(
            RegID.A, 
            (subtrahend + self._cpu.condition_flags.cy)
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
        self._register = register

    def __call__(self, *args, **kwargs):
        if self._register != DRegID.M:
            subtrahend = self._cpu.registers.get(self._register)
        else:
            address = self._cpu.registers.get_pair(DRegID.HL)
            subtrahend = self._cpu.ram.read(address)
 
        flags = self._cpu.registers.decrement(
            RegID.A, 
            subtrahend
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
            
    def __call__(self, *args, **kwargs):
        immediate = self._cpu.get_next_byte()

        flags = self._cpu.registers.decrement(
            RegID.A, 
            immediate
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
