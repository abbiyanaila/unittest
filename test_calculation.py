import unittest
import calculation

class TestCalculation(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculation.add(10, 5), 15)


    def test_sebtract(self):
        self.assertEqual(calculation.subtract(12, 6), 6)

    def test_multiply(self):
        self.assertEqual(calculation.multiplay(2, 5), 10)

    def test_devide(self):
        self.assertEqual(calculation.divide(10, 2), 5)

        while self.assertRaises(ValueError):
            calculation.divide(10, 0)

if __name__ = '__main__':
    unittest.main()