import unittest
from hello import greet, sum_numbers

def get_remaining_iterations(n, total):
    return total - n

class TestHello(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(greet("World"), "Hello World")
        self.assertEqual(greet("Python"), "Hello Python")
        self.assertEqual(greet(""), "Hello ")

    def test_sum(self):
        self.assertEqual(sum_numbers(2, 3), 5)
        self.assertEqual(sum_numbers(0, 0), 0)
        self.assertEqual(sum_numbers(-1, 1), 0)
        self.assertEqual(sum_numbers(10, -5), 5)

    def test_get_remaining_iterations(self):
        self.assertEqual(get_remaining_iterations(1, 3), 2)
        self.assertEqual(get_remaining_iterations(2, 5), 3)
        self.assertEqual(get_remaining_iterations(0, 2), 2)
        self.assertEqual(get_remaining_iterations(3, 3), 0)


if __name__ == '__main__':
    unittest.main()

