import unittest

class SomeTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(3, 3)

if __name__ == "__main__":
    unittest.main()
