import unittest
from mathematics import Mathematics

class MysTestCase(unittest.TestCase):

    def setUp(self):
        self.math = Mathematics()

    def test_first(self):
        result = self.math.sumoftwonumber(12,23)
        self.assertEqual(result, 35)

    def test_second(self):
        result = self.math.multiplytwonumber(4, 5)
        self.assertEqual(result, 20)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
