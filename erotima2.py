import unittest
from erotima1 import checkiftriangle, median, mean, stdev, embadon


class TestTriangles(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(checkiftriangle(), 161672)
        self.assertAlmostEqual(round(mean(embadon),2), 3206.84)
        self.assertAlmostEqual(median(embadon), 2392.50)
        self.assertAlmostEqual(round(stdev(embadon),2), 2843.24)


if __name__ == "__main__":
    unittest.main()
