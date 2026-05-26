import unittest
from merge_data import merge_data

class TestCases(unittest.TestCase):

    def test_example1(self):
        cd1 = [101,104,107,0,0,0]
        cd2 = [102,105,108]
        merge_data(cd1, 3, cd2, 3)
        self.assertEqual(cd1, [101, 102, 104, 105, 107, 108])

    def test_cd2_greaterthan_cd1(self):
        cd1 = [101,104,107,0,0,0,0,0]
        cd2 = [102,105,108,110,140]
        merge_data(cd1, 3, cd2, 5)
        self.assertEqual(cd1, [101, 102, 104, 105, 107, 108, 110, 140])

    def test_cd1_greaterthan_cd2(self):
        cd1 = [101,104,107,140,160,0,0,0]
        cd2 = [102,105,108]
        merge_data(cd1, 5, cd2, 3)
        self.assertEqual(cd1, [101, 102, 104, 105, 107, 108, 140, 160])

    def test_bothempty(self):
        cd1 = []
        merge_data(cd1, 0, [], 0)
        self.assertEqual(cd1, [])

    def test_cd1_empty(self):
        cd1 = [0,0,0]
        cd2 = [102,105,108]
        merge_data(cd1, 0, cd2, 3)
        self.assertEqual(cd1, [102, 105, 108])

    def test_cd2_empty(self):
        cd1 = [101,104,107]
        cd2 = []
        merge_data(cd1, 3, cd2, 0)
        self.assertEqual(cd1, [101, 104, 107])

if __name__ == "__main__":
    unittest.main()