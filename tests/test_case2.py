import unittest

class TestCase2(unittest.TestCase):
    def test_feature_b(self):
        self.assertTrue("SQMA".islower() is False)

if __name__ == "__main__":
    unittest.main()