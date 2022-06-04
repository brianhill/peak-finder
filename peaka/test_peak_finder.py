import unittest
from peak_finder import PeakFinder


class MyTestCase(unittest.TestCase):
    def test_find_peak(self):
        data = [0.0, 0.2, 0.1]
        pf = PeakFinder()
        location = pf.find_peak(data)
        expected = 1
        self.assertEqual(expected, location)


if __name__ == '__main__':
    unittest.main()
