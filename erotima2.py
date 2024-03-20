import unittest
from erotima1 import checkiftriangle, median, mean, stdev, embadon


class TestTriangles(unittest.TestCase):
    def test(self):
        self.assertEqual(checkiftriangle(), 161672)
        self.assertEqual(mean(embadon), 3206.83)
        self.assertEqual(median(embadon), 2392.50)
        self.assertEqual(stdev(embadon), 2843.24)


if __name__ == "__main__":
    unittest.main()
