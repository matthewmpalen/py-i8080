# Python
from threading import Thread

# External
from numpy import uint8

# Local
import core.cpu.instructions as instr
from core.opcodes import Opcode
from .flags import Flag
from .registers import Register

class CPU(Thread):
    def __init__(self, *args, **kwargs):
        Thread.__init__(self, *args, **kwargs)
        self._registers = {
            'a': Register(uint8), 
            'b': Register(uint8), 
            'c': Register(uint8), 
            'd': Register(uint8), 
            'e': Register(uint8), 
            'h': Register(uint8), 
            'l': Register(uint8)
        }

        self._flags = {
            's': Flag(uint8), 
            'z': Flag(uint8), 
            'p': Flag(uint8), 
            'c': Flag(uint8), 
            'ac': Flag(uint8), 
            'pad': Flag(uint8)
        }

        self._sp = Register(uint8)
        self._pc = Register(uint8)

        self._instructions = {
            Opcode.NOP:     instr.NOPInstruction(self), 
            Opcode.LXI_B:   instr.LXIInstruction(self), 
            Opcode.STAX_B:  instr.STAXInstruction(self), 
            Opcode.INX_B:   instr.INXInstruction(self), 
            Opcode.INR_B:   instr.INRInstruction(self), 
            Opcode.DCR_B:   instr.DCRInstruction(self), 
            Opcode.MVI_B:   instr.MVIInstruction(self), 
            Opcode.RLC:     instr.RLCInstruction(self), 
            Opcode.NOP_8:   instr.NOPInstruction(self), 
            Opcode.DAD_B:   instr.DADInstruction(self), 
            Opcode.LDAX_B:  instr.LDAXInstruction(self), 
            Opcode.DCX_B:   instr.DCXInstruction(self), 
            Opcode.INR_C:   instr.INRInstruction(self), 
            Opcode.DCR_C:   instr.DCRInstruction(self), 
            Opcode.MVI_C:   instr.MVIInstruction(self), 
            Opcode.RRC:     instr.RRCInstruction(self), 

            Opcode.NOP_10:  instr.NOPInstruction(self), 
            Opcode.LXI_D:   instr.LXIInstruction(self), 
            Opcode.STAX_D:  instr.STAXInstruction(self), 
            Opcode.INX_D:   instr.INXInstruction(self), 
            Opcode.INR_D:   instr.INRInstruction(self), 
            Opcode.DCR_D:   instr.DCRInstruction(self), 
            Opcode.MVI_D:   instr.MVIInstruction(self), 
            Opcode.RAL:     instr.RALInstruction(self), 
            Opcode.NOP_18:  instr.NOPInstruction(self), 
            Opcode.DAD_D:   instr.DADInstruction(self), 
            Opcode.LDAX_D:  instr.LDAXInstruction(self), 
            Opcode.DCX_D:   instr.DCXInstruction(self), 
            Opcode.INR_E:   instr.INRInstruction(self), 
            Opcode.DCR_E:   instr.DCRInstruction(self), 
            Opcode.MVI_E:   instr.MVIInstruction(self), 
            Opcode.RAR:     instr.RARInstruction(self), 

            0x20: instr.NOPInstruction(self), 
            0x21: instr.LXIInstruction(self), 
            0x22: instr.SHLDInstruction(self), 
            0x23: instr.INXInstruction(self), 
            0x24: instr.INRInstruction(self), 
            0x25: instr.DCRInstruction(self), 
            0x26: instr.MVIInstruction(self), 
            0x27: instr.DAAInstruction(self), 
            0x28: instr.NOPInstruction(self), 
            0x29: instr.DADInstruction(self), 
            0x2a: instr.LHLDInstruction(self), 
            0x2b: instr.DCXInstruction(self), 
            0x2c: instr.INRInstruction(self), 
            0x2d: instr.DCRInstruction(self), 
            0x2e: instr.MVIInstruction(self), 
            0x2f: instr.CMAInstruction(self), 

            0x30: instr.NOPInstruction(self), 
            0x31: instr.LXIInstruction(self), 
            0x32: instr.STAInstruction(self), 
            0x33: instr.INXInstruction(self), 
            0x34: instr.INRInstruction(self), 
            0x35: instr.DCRInstruction(self), 
            0x36: instr.MVIInstruction(self), 
            0x37: instr.STCInstruction(self), 
            0x38: instr.NOPInstruction(self), 
            0x39: instr.DADInstruction(self), 
            0x3a: instr.LDAInstruction(self), 
            0x3b: instr.DCXInstruction(self), 
            0x3c: instr.INRInstruction(self), 
            0x3d: instr.DCRInstruction(self), 
            0x3e: instr.MVIInstruction(self), 
            0x3f: instr.CMCInstruction(self), 

            0x40: instr.MOVInstruction(self), 
            0x41: instr.MOVInstruction(self), 
            0x42: instr.MOVInstruction(self), 
            0x43: instr.MOVInstruction(self), 
            0x44: instr.MOVInstruction(self), 
            0x45: instr.MOVInstruction(self), 
            0x46: instr.MOVInstruction(self), 
            0x47: instr.MOVInstruction(self), 
            0x48: instr.MOVInstruction(self), 
            0x49: instr.MOVInstruction(self), 
            0x4a: instr.MOVInstruction(self), 
            0x4b: instr.MOVInstruction(self), 
            0x4c: instr.MOVInstruction(self), 
            0x4d: instr.MOVInstruction(self), 
            0x4e: instr.MOVInstruction(self), 
            0x4f: instr.MOVInstruction(self), 

            0x50: instr.MOVInstruction(self), 
            0x51: instr.MOVInstruction(self), 
            0x52: instr.MOVInstruction(self), 
            0x53: instr.MOVInstruction(self), 
            0x54: instr.MOVInstruction(self), 
            0x55: instr.MOVInstruction(self), 
            0x56: instr.MOVInstruction(self), 
            0x57: instr.MOVInstruction(self), 
            0x58: instr.MOVInstruction(self), 
            0x59: instr.MOVInstruction(self), 
            0x5a: instr.MOVInstruction(self), 
            0x5b: instr.MOVInstruction(self), 
            0x5c: instr.MOVInstruction(self), 
            0x5d: instr.MOVInstruction(self), 
            0x5e: instr.MOVInstruction(self), 
            0x5f: instr.MOVInstruction(self), 

            0x60: instr.MOVInstruction(self), 
            0x61: instr.MOVInstruction(self), 
            0x62: instr.MOVInstruction(self), 
            0x63: instr.MOVInstruction(self), 
            0x64: instr.MOVInstruction(self), 
            0x65: instr.MOVInstruction(self), 
            0x66: instr.MOVInstruction(self), 
            0x67: instr.MOVInstruction(self), 
            0x68: instr.MOVInstruction(self), 
            0x69: instr.MOVInstruction(self), 
            0x6a: instr.MOVInstruction(self), 
            0x6b: instr.MOVInstruction(self), 
            0x6c: instr.MOVInstruction(self), 
            0x6d: instr.MOVInstruction(self), 
            0x6e: instr.MOVInstruction(self), 
            0x6f: instr.MOVInstruction(self), 

            0x70: instr.MOVInstruction(self), 
            0x71: instr.MOVInstruction(self), 
            0x72: instr.MOVInstruction(self), 
            0x73: instr.MOVInstruction(self), 
            0x74: instr.MOVInstruction(self), 
            0x75: instr.MOVInstruction(self), 

            0x76: instr.HLTInstruction(self), 

            0x77: instr.MOVInstruction(self), 
            0x78: instr.MOVInstruction(self), 
            0x79: instr.MOVInstruction(self), 
            0x7a: instr.MOVInstruction(self), 
            0x7b: instr.MOVInstruction(self), 
            0x7c: instr.MOVInstruction(self), 
            0x7d: instr.MOVInstruction(self), 
            0x7e: instr.MOVInstruction(self), 
            0x7f: instr.MOVInstruction(self), 

            0x80: instr.ADDInstruction(self), 
            0x81: instr.ADDInstruction(self), 
            0x82: instr.ADDInstruction(self), 
            0x83: instr.ADDInstruction(self), 
            0x84: instr.ADDInstruction(self), 
            0x85: instr.ADDInstruction(self), 
            0x86: instr.ADDInstruction(self), 
            0x87: instr.ADDInstruction(self),

            0x88: instr.ADCInstruction(self), 
            0x89: instr.ADCInstruction(self), 
            0x8a: instr.ADCInstruction(self), 
            0x8b: instr.ADCInstruction(self), 
            0x8c: instr.ADCInstruction(self), 
            0x8d: instr.ADCInstruction(self), 
            0x8e: instr.ADCInstruction(self), 
            0x8f: instr.ADCInstruction(self), 

            0x90: instr.SUBInstruction(self), 
            0x91: instr.SUBInstruction(self), 
            0x92: instr.SUBInstruction(self), 
            0x93: instr.SUBInstruction(self), 
            0x94: instr.SUBInstruction(self), 
            0x95: instr.SUBInstruction(self), 
            0x96: instr.SUBInstruction(self), 
            0x97: instr.SUBInstruction(self), 

            0x98: instr.SBBInstruction(self), 
            0x99: instr.SBBInstruction(self), 
            0x9a: instr.SBBInstruction(self), 
            0x9b: instr.SBBInstruction(self), 
            0x9c: instr.SBBInstruction(self), 
            0x9d: instr.SBBInstruction(self), 
            0x9e: instr.SBBInstruction(self), 
            0x9f: instr.SBBInstruction(self), 

            0xa0: instr.ANAInstruction(self), 
            0xa1: instr.ANAInstruction(self), 
            0xa2: instr.ANAInstruction(self), 
            0xa3: instr.ANAInstruction(self), 
            0xa4: instr.ANAInstruction(self), 
            0xa5: instr.ANAInstruction(self), 
            0xa6: instr.ANAInstruction(self), 
            0xa7: instr.ANAInstruction(self), 

            0xa8: instr.XRAInstruction(self), 
            0xa9: instr.XRAInstruction(self), 
            0xaa: instr.XRAInstruction(self), 
            0xab: instr.XRAInstruction(self), 
            0xac: instr.XRAInstruction(self), 
            0xad: instr.XRAInstruction(self), 
            0xae: instr.XRAInstruction(self), 
            0xaf: instr.XRAInstruction(self), 

            0xb0: instr.ORAInstruction(self), 
            0xb1: instr.ORAInstruction(self), 
            0xb2: instr.ORAInstruction(self), 
            0xb3: instr.ORAInstruction(self), 
            0xb4: instr.ORAInstruction(self), 
            0xb5: instr.ORAInstruction(self), 
            0xb6: instr.ORAInstruction(self), 
            0xb7: instr.ORAInstruction(self), 

            0xb8: instr.CMPInstruction(self), 
            0xb9: instr.CMPInstruction(self), 
            0xba: instr.CMPInstruction(self), 
            0xbb: instr.CMPInstruction(self), 
            0xbc: instr.CMPInstruction(self), 
            0xbd: instr.CMPInstruction(self), 
            0xbe: instr.CMPInstruction(self), 
            0xbf: instr.CMPInstruction(self), 

            0xc0: instr.RNZInstruction(self), 
            0xc1: instr.POPInstruction(self), 
            0xc2: instr.JNZInstruction(self), 
            0xc3: instr.JMPInstruction(self), 
            0xc4: instr.CNZInstruction(self), 
            0xc5: instr.PUSHInstruction(self), 
            0xc6: instr.ADIInstruction(self), 
            0xc7: instr.RSTInstruction(self), 
            0xc8: instr.RZInstruction(self), 
            0xc9: instr.RETInstruction(self), 
            0xca: instr.JZInstruction(self), 
            0xcb: instr.JMPInstruction(self), 
            0xcc: instr.CZInstruction(self), 
            0xcd: instr.CALLInstruction(self), 
            0xce: instr.ACIInstruction(self), 
            0xcf: instr.RSTInstruction(self), 

            0xd0: instr.RNCInstruction(self), 
            0xd1: instr.POPInstruction(self), 
            0xd2: instr.JNCInstruction(self), 
            0xd3: instr.OUTInstruction(self), 
            0xd4: instr.CNCInstruction(self), 
            0xd5: instr.PUSHInstruction(self), 
            0xd6: instr.SUIInstruction(self), 
            0xd7: instr.RSTInstruction(self), 
            0xd8: instr.RCInstruction(self), 
            0xd9: instr.RETInstruction(self), 
            0xda: instr.JCInstruction(self), 
            0xdb: instr.INInstruction(self), 
            0xdc: instr.CCInstruction(self), 
            0xdd: instr.CALLInstruction(self), 
            0xde: instr.SBIInstruction(self), 
            0xdf: instr.RSTInstruction(self), 

            0xe0: instr.RPOInstruction(self), 
            0xe1: instr.POPInstruction(self), 
            0xe2: instr.JPOInstruction(self), 
            0xe3: instr.XTHLInstruction(self), 
            0xe4: instr.CPOInstruction(self), 
            0xe5: instr.PUSHInstruction(self), 
            0xe6: instr.ANIInstruction(self), 
            0xe7: instr.RSTInstruction(self), 
            0xe8: instr.RPEInstruction(self), 
            0xe9: instr.PCHLInstruction(self), 
            0xea: instr.JPEInstruction(self), 
            0xeb: instr.XCHGInstruction(self), 
            0xec: instr.CPEInstruction(self), 
            0xed: instr.CALLInstruction(self), 
            0xee: instr.XRIInstruction(self), 
            0xef: instr.RSTInstruction(self), 

            0xf0: instr.RPInstruction(self), 
            0xf1: instr.POPInstruction(self), 
            0xf2: instr.JPInstruction(self), 
            0xf3: instr.DIInstruction(self), 
            0xf4: instr.CPInstruction(self), 
            0xf5: instr.PUSHInstruction(self), 
            0xf6: instr.ORIInstruction(self), 
            0xf7: instr.RSTInstruction(self), 
            0xf8: instr.RMInstruction(self), 
            0xf9: instr.SPHLInstruction(self), 
            0xfa: instr.JMInstruction(self), 
            0xfb: instr.EIInstruction(self), 
            0xfc: instr.CMInstruction(self), 
            0xfd: instr.CALLInstruction(self), 
            0xfe: instr.CPIInstruction(self), 
            0xff: instr.RSTInstruction(self) 
        }

    def run(self):
        print('Running CPU')
