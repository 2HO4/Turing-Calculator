# TEST CALCULATOR
# ----------------------------------------------------------------------------------------------------------------


# START --------
import unittest
from TuringCalculator import Calculator


# EXECUTION ----
class MyTestCase(unittest.TestCase):
    def test_add(self, calculator=Calculator()):
        calculator.add(2.4)
        self.assertEqual(calculator.getResult(), 2.4)


if __name__ == '__main__':
    unittest.main()
