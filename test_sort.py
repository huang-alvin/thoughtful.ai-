import unittest
from index import sort, Status

class TestSort(unittest.TestCase):
    def test_special_max_volume(self):
        res = sort(120, 100, 100, 10)
        self.assertEqual(res, Status.SPECIAL)
    
    def test_special_max_dimension(self):
        res = sort(300, 1, 1, 1)
        self.assertEqual(res, Status.SPECIAL)
    
    def test_special_heavy(self):
        res = sort(2, 100, 4, 100)
        self.assertEqual(res, Status.SPECIAL)
    
    def test_reject_with_max_volume(self):
        res = sort(120, 100, 100, 30)
        self.assertEqual(res, Status.REJECTED)
    
    def test_reject_with_max_dimension(self):
        res = sort(190, 10, 10, 30)
        self.assertEqual(res, Status.REJECTED)
    
    def test_standard(self):
        res = sort(10,10,10,10)
        self.assertEqual(res, Status.STANDARD)

if __name__ == '__main__':
    unittest.main()