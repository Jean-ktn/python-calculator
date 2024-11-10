import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()
        

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def testadd2(self):
        self.assertEqual(self.calc.add(50, 33), 83)

    def testsubtract1(self):
        self.assertEqual(self.calc.subtract(4, 8), 4)
    def testsubtract2(self):
        self.assertEqual(self.calc.subtract(46, 26), -20)

    def test_multiply1(self):
        self.assertEqual(self.calc.multiply(9, 4), 36)
    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(0, 1), 0)

    def test_divide1(self):
        self.assertEqual(self.calc.divide(8, 8), 1)
    def test_divide2(self):
        self.assertEqual(self.calc.divide(40, 5), 8)

    def test_modulo1(self):
        self.assertEqual(self.calc.modulo(7, 3), 1)
    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(63, 8), 7)

if __name__ == '__main__':
    unittest.main()