import unittest
from utils import utils


class TestUtils(unittest.TestCase):

    def test_reversed_integer(self):
        self.assertEqual(utils.reversed(12345), 54321)
        self.assertEqual(utils.reversed(100), 1)
        self.assertEqual(utils.reversed(-123), -321)

    def test_reversed_string(self):
        with self.assertRaises(TypeError):
            utils.reversed("12345")

    def test_reversed_float(self):
        with self.assertRaises(TypeError):
            utils.reversed(123.45)

    def test_formatter_integer(self):
        self.assertEqual(utils.formatter(10), ("0b1010", "0o12"))
        self.assertEqual(utils.formatter(8), ("0b1000", "0o10"))

    def test_formatter_string(self):
        with self.assertRaises(TypeError):
            utils.formatter("10")

    def test_formatter_float(self):
        with self.assertRaises(TypeError):
            utils.formatter(10.5)


if __name__ == "__main__":
    unittest.main()