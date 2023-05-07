import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
radius = 6
pi = 3.14159
surface = pi * radius * 2
print(2*pi*radius)