# Python
from unittest import TestCase

# External

# Local
from .registers import RegID, DRegID, Registers

class RegistersAndTestCase(TestCase):
    def setUp(self):
        self.registers = Registers()

    def test_and_zero(self):
        self.registers.set(RegID.A, 0x3a)
        flags = self.registers.and_(RegID.A, 0x00)
        self.assertEqual(self.registers.get(RegID.A), 0x00)

    def test_and_one(self):
        self.registers.set(RegID.A, 0x3a)
        flags = self.registers.and_(RegID.A, 0x0f)
        self.assertEqual(self.registers.get(RegID.A),  0x0a)

class RegisterOrTestCase(TestCase):
    def setUp(self):
        self.registers = Registers()

    def test_or_0x00(self):
        self.registers.set(RegID.A, 0xb5)
        flags = self.registers.or_(RegID.A, 0x00)
        self.assertEqual(self.registers.get(RegID.A), 0xb5)

    def test_or_0x0f(self):
        self.registers.set(RegID.A, 0xb5)
        flags = self.registers.or_(RegID.A, 0x0f)
        self.assertEqual(self.registers.get(RegID.A), 0xbf)

class RegisterXorTestCase(TestCase):
    def setUp(self):
        self.registers = Registers()

    def test_xor_0x00(self):
        self.registers.set(RegID.A, 0x3b)
        flags = self.registers.xor_(RegID.A, 0x81)
        self.assertEqual(self.registers.get(RegID.A), 0xba)

class RegisterNotTestCase(TestCase):
    def setUp(self):
        self.registers = Registers()

    def test_not_0x00(self):
        self.registers.set(RegID.A, 0x00)
        flags = self.registers.not_(RegID.A)
        self.assertEqual(self.registers.get(RegID.A), 0xff)

    def test_not_0xff(self):
        self.registers.set(RegID.A, 0xff)
        flags = self.registers.not_(RegID.A)
        self.assertEqual(self.registers.get(RegID.A), 0x00)

class RegistersShiftLeftTestCase(TestCase):
    def setUp(self):
        self.registers = Registers()

    def test_shift_left_high_bit_0(self):
        self.registers.set(RegID.A, 0x70)
        flags = self.registers.shift_left_(RegID.A)
        self.assertEqual(self.registers.get(RegID.A), 0xe0)
        self.assertEqual(flags['cy'], False)

    def test_shift_left_high_bit_1(self):
        self.registers.set(RegID.A, 0xf2)
        flags = self.registers.shift_left_(RegID.A)
        self.assertEqual(self.registers.get(RegID.A), 0xe5)
        self.assertEqual(flags['cy'], True)

class RegisterShiftLeftCarryTestCase(TestCase):
    def setUp(self):
        self.registers = Registers()

    def test_shift_left_carry_high_bit_0(self):
        self.registers.set(RegID.A, 0x75)
        cy = False
        flags = self.registers.shift_left_carry_(RegID.A, cy)
        self.assertEqual(self.registers.get(RegID.A), 0xea)
        self.assertEqual(flags['cy'], False)

    def test_shift_left_carry_high_bit_1(self):
        self.registers.set(RegID.A, 0xb5)
        cy = False
        flags = self.registers.shift_left_carry_(RegID.A, cy)
        self.assertEqual(self.registers.get(RegID.A), 0x6a)
        self.assertEqual(flags['cy'], True)

class RegistersShiftRightTestCase(TestCase):
    def setUp(self):
        self.registers = Registers()

    def test_shift_right_low_bit_0(self):
        self.registers.set(RegID.A, 0xf2)
        flags = self.registers.shift_right_(RegID.A)
        self.assertEqual(self.registers.get(RegID.A), 0x79)
        self.assertEqual(flags['cy'], False)

    def test_shift_right_low_bit_1(self):
        self.registers.set(RegID.A, 0xf3)
        flags = self.registers.shift_right_(RegID.A)
        self.assertEqual(self.registers.get(RegID.A), 0xf9)
        self.assertEqual(flags['cy'], True)
