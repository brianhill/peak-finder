import unittest
from peak_finder import PeakFinder


class MyTestCase(unittest.TestCase):
    def test_find_peak(self):
        data = None
        pf = PeakFinder()
        location = pf.find_peak(data)
        expected = 0
        self.assertEqual(0, location)


if __name__ == '__main__':
    unittest.main()
