import unittest
from simple_math import SimpleMath


class TestSimpleMath(unittest.TestCase):

    def setUp(self):
        self.math = SimpleMath()

    def test_square_positive(self):
        self.assertEqual(self.math.square(2), 4)
        self.assertEqual(self.math.square(5), 25)

    def test_square_negative(self):
        self.assertEqual(self.math.square(-3), 9)

    def test_square_zero(self):
        self.assertEqual(self.math.square(0), 0)

    def test_cube_positive(self):
        self.assertEqual(self.math.cube(3), 27)

    def test_cube_negative(self):
        self.assertEqual(self.math.cube(-3), -27)

    def test_cube_zero(self):
        self.assertEqual(self.math.cube(0), 0)


if __name__ == "__main__":
    unittest.main()