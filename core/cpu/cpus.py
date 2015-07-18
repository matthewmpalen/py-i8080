# Python
from threading import Thread

# Local
import core.cpu.instructions as instr
from core.opcodes import Opcode
from .flags import ConditionFlags
from .registers import Register

class CPU(Thread):
    def __init__(self, *args, **kwargs):
        Thread.__init__(self, *args, **kwargs)

        self._a = Register()
        self._b = Register()
        self._c = Register()
        self._d = Register()
        self._e = Register()
        self._h = Register()
        self._l = Register()

        self._condition_flags = ConditionFlags()

        self._sp = Register()
        self._pc = Register()

        self._data = None

        self._instructions = {
            Opcode.NOP:         instr.NOPInstruction(self), 
            Opcode.LXI_B:       instr.LXIInstruction(self), 
            Opcode.STAX_B:      instr.STAXInstruction(self), 
            Opcode.INX_B:       instr.INXInstruction(self), 
            Opcode.INR_B:       instr.INRInstruction(self), 
            Opcode.DCR_B:       instr.DCRInstruction(self), 
            Opcode.MVI_B:       instr.MVIInstruction(self), 
            Opcode.RLC:         instr.RLCInstruction(self), 
            Opcode.NOP_8:       instr.NOPInstruction(self), 
            Opcode.DAD_B:       instr.DADInstruction(self), 
            Opcode.LDAX_B:      instr.LDAXInstruction(self), 
            Opcode.DCX_B:       instr.DCXInstruction(self), 
            Opcode.INR_C:       instr.INRInstruction(self), 
            Opcode.DCR_C:       instr.DCRInstruction(self), 
            Opcode.MVI_C:       instr.MVIInstruction(self), 
            Opcode.RRC:         instr.RRCInstruction(self), 

            Opcode.NOP_10:      instr.NOPInstruction(self), 
            Opcode.LXI_D:       instr.LXIInstruction(self), 
            Opcode.STAX_D:      instr.STAXInstruction(self), 
            Opcode.INX_D:       instr.INXInstruction(self), 
            Opcode.INR_D:       instr.INRInstruction(self), 
            Opcode.DCR_D:       instr.DCRInstruction(self), 
            Opcode.MVI_D:       instr.MVIInstruction(self), 
            Opcode.RAL:         instr.RALInstruction(self), 
            Opcode.NOP_18:      instr.NOPInstruction(self), 
            Opcode.DAD_D:       instr.DADInstruction(self), 
            Opcode.LDAX_D:      instr.LDAXInstruction(self), 
            Opcode.DCX_D:       instr.DCXInstruction(self), 
            Opcode.INR_E:       instr.INRInstruction(self), 
            Opcode.DCR_E:       instr.DCRInstruction(self), 
            Opcode.MVI_E:       instr.MVIInstruction(self), 
            Opcode.RAR:         instr.RARInstruction(self), 

            Opcode.NOP_20:      instr.NOPInstruction(self), 
            Opcode.LXI_H:       instr.LXIInstruction(self), 
            Opcode.SHLD:        instr.SHLDInstruction(self), 
            Opcode.INX_H:       instr.INXInstruction(self), 
            Opcode.INR_H:       instr.INRInstruction(self), 
            Opcode.DCR_H:       instr.DCRInstruction(self), 
            Opcode.MVI_H:       instr.MVIInstruction(self), 
            Opcode.DAA:         instr.DAAInstruction(self), 
            Opcode.NOP_28:      instr.NOPInstruction(self), 
            Opcode.DAD_H:       instr.DADInstruction(self), 
            Opcode.LHLD:        instr.LHLDInstruction(self), 
            Opcode.DCX_H:       instr.DCXInstruction(self), 
            Opcode.INR_L:       instr.INRInstruction(self), 
            Opcode.DCR_L:       instr.DCRInstruction(self), 
            Opcode.MVI_L:       instr.MVIInstruction(self), 
            Opcode.CMA:         instr.CMAInstruction(self), 

            Opcode.NOP_30:      instr.NOPInstruction(self), 
            Opcode.LXI_SP:      instr.LXIInstruction(self), 
            Opcode.STA:         instr.STAInstruction(self), 
            Opcode.INX_SP:      instr.INXInstruction(self), 
            Opcode.INR_M:       instr.INRInstruction(self), 
            Opcode.DCR_M:       instr.DCRInstruction(self), 
            Opcode.MVI_M:       instr.MVIInstruction(self), 
            Opcode.STC:         instr.STCInstruction(self), 
            Opcode.NOP_38:      instr.NOPInstruction(self), 
            Opcode.DAD_SP:      instr.DADInstruction(self), 
            Opcode.LDA:         instr.LDAInstruction(self), 
            Opcode.DCX_SP:      instr.DCXInstruction(self), 
            Opcode.INR_A:       instr.INRInstruction(self), 
            Opcode.DCR_A:       instr.DCRInstruction(self), 
            Opcode.MVI_A:       instr.MVIInstruction(self), 
            Opcode.CMC:         instr.CMCInstruction(self), 

            Opcode.MOV_B_B:     instr.MOVInstruction(self), 
            Opcode.MOV_B_C:     instr.MOVInstruction(self), 
            Opcode.MOV_B_D:     instr.MOVInstruction(self), 
            Opcode.MOV_B_E:     instr.MOVInstruction(self), 
            Opcode.MOV_B_H:     instr.MOVInstruction(self), 
            Opcode.MOV_B_L:     instr.MOVInstruction(self), 
            Opcode.MOV_B_M:     instr.MOVInstruction(self), 
            Opcode.MOV_B_A:     instr.MOVInstruction(self), 
            Opcode.MOV_C_B:     instr.MOVInstruction(self), 
            Opcode.MOV_C_C:     instr.MOVInstruction(self), 
            Opcode.MOV_C_D:     instr.MOVInstruction(self), 
            Opcode.MOV_C_E:     instr.MOVInstruction(self), 
            Opcode.MOV_C_H:     instr.MOVInstruction(self), 
            Opcode.MOV_C_L:     instr.MOVInstruction(self), 
            Opcode.MOV_C_M:     instr.MOVInstruction(self), 
            Opcode.MOV_C_A:     instr.MOVInstruction(self), 

            Opcode.MOV_D_B:     instr.MOVInstruction(self), 
            Opcode.MOV_D_C:     instr.MOVInstruction(self), 
            Opcode.MOV_D_D:     instr.MOVInstruction(self), 
            Opcode.MOV_D_E:     instr.MOVInstruction(self), 
            Opcode.MOV_D_H:     instr.MOVInstruction(self), 
            Opcode.MOV_D_L:     instr.MOVInstruction(self), 
            Opcode.MOV_D_M:     instr.MOVInstruction(self), 
            Opcode.MOV_D_A:     instr.MOVInstruction(self), 
            Opcode.MOV_E_B:     instr.MOVInstruction(self), 
            Opcode.MOV_E_C:     instr.MOVInstruction(self), 
            Opcode.MOV_E_D:     instr.MOVInstruction(self), 
            Opcode.MOV_E_E:     instr.MOVInstruction(self), 
            Opcode.MOV_E_H:     instr.MOVInstruction(self), 
            Opcode.MOV_E_L:     instr.MOVInstruction(self), 
            Opcode.MOV_E_M:     instr.MOVInstruction(self), 
            Opcode.MOV_E_A:     instr.MOVInstruction(self), 

            Opcode.MOV_H_B:     instr.MOVInstruction(self), 
            Opcode.MOV_H_C:     instr.MOVInstruction(self), 
            Opcode.MOV_H_D:     instr.MOVInstruction(self), 
            Opcode.MOV_H_E:     instr.MOVInstruction(self), 
            Opcode.MOV_H_H:     instr.MOVInstruction(self), 
            Opcode.MOV_H_L:     instr.MOVInstruction(self), 
            Opcode.MOV_H_M:     instr.MOVInstruction(self), 
            Opcode.MOV_H_A:     instr.MOVInstruction(self), 
            Opcode.MOV_L_B:     instr.MOVInstruction(self), 
            Opcode.MOV_L_C:     instr.MOVInstruction(self), 
            Opcode.MOV_L_D:     instr.MOVInstruction(self), 
            Opcode.MOV_L_E:     instr.MOVInstruction(self), 
            Opcode.MOV_L_H:     instr.MOVInstruction(self), 
            Opcode.MOV_L_L:     instr.MOVInstruction(self), 
            Opcode.MOV_L_M:     instr.MOVInstruction(self), 
            Opcode.MOV_L_A:     instr.MOVInstruction(self), 

            Opcode.MOV_M_B:     instr.MOVInstruction(self), 
            Opcode.MOV_M_C:     instr.MOVInstruction(self), 
            Opcode.MOV_M_D:     instr.MOVInstruction(self), 
            Opcode.MOV_M_E:     instr.MOVInstruction(self), 
            Opcode.MOV_M_H:     instr.MOVInstruction(self), 
            Opcode.MOV_M_L:     instr.MOVInstruction(self), 

            Opcode.HLT:         instr.HLTInstruction(self), 

            Opcode.MOV_M_A:     instr.MOVInstruction(self), 
            Opcode.MOV_A_B:     instr.MOVInstruction(self), 
            Opcode.MOV_A_C:     instr.MOVInstruction(self), 
            Opcode.MOV_A_D:     instr.MOVInstruction(self), 
            Opcode.MOV_A_E:     instr.MOVInstruction(self), 
            Opcode.MOV_A_H:     instr.MOVInstruction(self), 
            Opcode.MOV_A_L:     instr.MOVInstruction(self), 
            Opcode.MOV_A_M:     instr.MOVInstruction(self), 
            Opcode.MOV_A_A:     instr.MOVInstruction(self), 

            Opcode.ADD_B:       instr.ADDInstruction(self), 
            Opcode.ADD_C:       instr.ADDInstruction(self), 
            Opcode.ADD_D:       instr.ADDInstruction(self), 
            Opcode.ADD_E:       instr.ADDInstruction(self), 
            Opcode.ADD_H:       instr.ADDInstruction(self), 
            Opcode.ADD_L:       instr.ADDInstruction(self), 
            Opcode.ADD_M:       instr.ADDInstruction(self), 
            Opcode.ADD_A:       instr.ADDInstruction(self),

            Opcode.ADC_B:       instr.ADCInstruction(self), 
            Opcode.ADC_C:       instr.ADCInstruction(self), 
            Opcode.ADC_D:       instr.ADCInstruction(self), 
            Opcode.ADC_E:       instr.ADCInstruction(self), 
            Opcode.ADC_H:       instr.ADCInstruction(self), 
            Opcode.ADC_L:       instr.ADCInstruction(self), 
            Opcode.ADC_M:       instr.ADCInstruction(self), 
            Opcode.ADC_A:       instr.ADCInstruction(self), 

            Opcode.SUB_B:       instr.SUBInstruction(self), 
            Opcode.SUB_C:       instr.SUBInstruction(self), 
            Opcode.SUB_D:       instr.SUBInstruction(self), 
            Opcode.SUB_E:       instr.SUBInstruction(self), 
            Opcode.SUB_H:       instr.SUBInstruction(self), 
            Opcode.SUB_L:       instr.SUBInstruction(self), 
            Opcode.SUB_M:       instr.SUBInstruction(self), 
            Opcode.SUB_A:       instr.SUBInstruction(self), 

            Opcode.SBB_B:       instr.SBBInstruction(self), 
            Opcode.SBB_C:       instr.SBBInstruction(self), 
            Opcode.SBB_D:       instr.SBBInstruction(self), 
            Opcode.SBB_E:       instr.SBBInstruction(self), 
            Opcode.SBB_H:       instr.SBBInstruction(self), 
            Opcode.SBB_L:       instr.SBBInstruction(self), 
            Opcode.SBB_M:       instr.SBBInstruction(self), 
            Opcode.SBB_A:       instr.SBBInstruction(self), 

            Opcode.ANA_B:       instr.ANAInstruction(self), 
            Opcode.ANA_C:       instr.ANAInstruction(self), 
            Opcode.ANA_D:       instr.ANAInstruction(self), 
            Opcode.ANA_E:       instr.ANAInstruction(self), 
            Opcode.ANA_H:       instr.ANAInstruction(self), 
            Opcode.ANA_L:       instr.ANAInstruction(self), 
            Opcode.ANA_M:       instr.ANAInstruction(self), 
            Opcode.ANA_A:       instr.ANAInstruction(self), 

            Opcode.XRA_B:       instr.XRAInstruction(self), 
            Opcode.XRA_C:       instr.XRAInstruction(self), 
            Opcode.XRA_D:       instr.XRAInstruction(self), 
            Opcode.XRA_E:       instr.XRAInstruction(self), 
            Opcode.XRA_H:       instr.XRAInstruction(self), 
            Opcode.XRA_L:       instr.XRAInstruction(self), 
            Opcode.XRA_M:       instr.XRAInstruction(self), 
            Opcode.XRA_A:       instr.XRAInstruction(self), 

            Opcode.ORA_B:       instr.ORAInstruction(self), 
            Opcode.ORA_C:       instr.ORAInstruction(self), 
            Opcode.ORA_D:       instr.ORAInstruction(self), 
            Opcode.ORA_E:       instr.ORAInstruction(self), 
            Opcode.ORA_H:       instr.ORAInstruction(self), 
            Opcode.ORA_L:       instr.ORAInstruction(self), 
            Opcode.ORA_M:       instr.ORAInstruction(self), 
            Opcode.ORA_A:       instr.ORAInstruction(self), 

            Opcode.CMP_B:       instr.CMPInstruction(self), 
            Opcode.CMP_C:       instr.CMPInstruction(self), 
            Opcode.CMP_D:       instr.CMPInstruction(self), 
            Opcode.CMP_E:       instr.CMPInstruction(self), 
            Opcode.CMP_H:       instr.CMPInstruction(self), 
            Opcode.CMP_L:       instr.CMPInstruction(self), 
            Opcode.CMP_M:       instr.CMPInstruction(self), 
            Opcode.CMP_A:       instr.CMPInstruction(self), 

            Opcode.RNZ:         instr.RNZInstruction(self), 
            Opcode.POP_B:       instr.POPInstruction(self), 
            Opcode.JNZ:         instr.JNZInstruction(self), 
            Opcode.JMP:         instr.JMPInstruction(self), 
            Opcode.CNZ:         instr.CNZInstruction(self), 
            Opcode.PUSH_B:      instr.PUSHInstruction(self), 
            Opcode.ADI:         instr.ADIInstruction(self), 
            Opcode.RST_0:       instr.RSTInstruction(self), 
            Opcode.RZ:          instr.RZInstruction(self), 
            Opcode.RET:         instr.RETInstruction(self), 
            Opcode.JZ:          instr.JZInstruction(self), 
            Opcode.JMP_CB:     instr.JMPInstruction(self), 
            Opcode.CZ:          instr.CZInstruction(self), 
            Opcode.CALL:        instr.CALLInstruction(self), 
            Opcode.ACI:         instr.ACIInstruction(self), 
            Opcode.RST_1:       instr.RSTInstruction(self), 

            Opcode.RNC:         instr.RNCInstruction(self), 
            Opcode.POP_D:       instr.POPInstruction(self), 
            Opcode.JNC:         instr.JNCInstruction(self), 
            Opcode.OUT:         instr.OUTInstruction(self), 
            Opcode.CNC:         instr.CNCInstruction(self), 
            Opcode.PUSH_D:      instr.PUSHInstruction(self), 
            Opcode.SUI:         instr.SUIInstruction(self), 
            Opcode.RST_2:       instr.RSTInstruction(self), 
            Opcode.RC:          instr.RCInstruction(self), 
            Opcode.RET_D9:      instr.RETInstruction(self), 
            Opcode.JC:          instr.JCInstruction(self), 
            Opcode.IN:          instr.INInstruction(self), 
            Opcode.CC:          instr.CCInstruction(self), 
            Opcode.CALL_DD:     instr.CALLInstruction(self), 
            Opcode.SBI:         instr.SBIInstruction(self), 
            Opcode.RST_3:       instr.RSTInstruction(self), 

            Opcode.RPO:         instr.RPOInstruction(self), 
            Opcode.POP_H:       instr.POPInstruction(self), 
            Opcode.JPO:         instr.JPOInstruction(self), 
            Opcode.XTHL:        instr.XTHLInstruction(self), 
            Opcode.CPO:         instr.CPOInstruction(self), 
            Opcode.PUSH_H:      instr.PUSHInstruction(self), 
            Opcode.ANI:         instr.ANIInstruction(self), 
            Opcode.RST_4:       instr.RSTInstruction(self), 
            Opcode.RPE:         instr.RPEInstruction(self), 
            Opcode.PCHL:        instr.PCHLInstruction(self), 
            Opcode.JPE:         instr.JPEInstruction(self), 
            Opcode.XCHG:        instr.XCHGInstruction(self), 
            Opcode.CPE:         instr.CPEInstruction(self), 
            Opcode.CALL_ED:     instr.CALLInstruction(self), 
            Opcode.XRI:         instr.XRIInstruction(self), 
            Opcode.RST_5:       instr.RSTInstruction(self), 

            Opcode.RP:          instr.RPInstruction(self), 
            Opcode.POP_PSW:     instr.POPInstruction(self), 
            Opcode.JP:          instr.JPInstruction(self), 
            Opcode.DI:          instr.DIInstruction(self), 
            Opcode.CP:          instr.CPInstruction(self), 
            Opcode.PUSH_PSW:    instr.PUSHInstruction(self), 
            Opcode.ORI:         instr.ORIInstruction(self), 
            Opcode.RST_6:       instr.RSTInstruction(self), 
            Opcode.RM:          instr.RMInstruction(self), 
            Opcode.SPHL:        instr.SPHLInstruction(self), 
            Opcode.JM:          instr.JMInstruction(self), 
            Opcode.EI:          instr.EIInstruction(self), 
            Opcode.CM:          instr.CMInstruction(self), 
            Opcode.CALL_FD:     instr.CALLInstruction(self), 
            Opcode.CPI:         instr.CPIInstruction(self), 
            Opcode.RST_7:       instr.RSTInstruction(self) 
        }

    def _fetch_instruction(self):
        pass

    def _execute(self, opcode):
        self._instructions[opcode]()

    def incrementProgramCounter(self, value):
        self._pc.increment(value)

    def load(self, rom):
        self._data = rom

    def run(self):
        print('Running CPU')
        while True:
            self._execute(self._pc.read())
