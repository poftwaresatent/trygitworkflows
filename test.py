import unittest

class SomeTest(unittest.TestCase):
    def test_something(self):
        # reading up on protected branches ...
        # https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests
        self.assertEqual(3, 44)

if __name__ == "__main__":
    unittest.main()
