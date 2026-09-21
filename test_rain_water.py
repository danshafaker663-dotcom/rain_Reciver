"""运行方式：python -m unittest -v"""

import unittest

from main import parse_heights
from rain_water import trap


class TestRainWater(unittest.TestCase):
    def test_examples_and_boundaries(self):
        cases = [
            ([], 0),
            ([3], 0),
            ([3, 2], 0),
            ([1, 2, 3, 4], 0),
            ([4, 3, 2, 1], 0),
            ([2, 2, 2], 0),
            ([3, 0, 3], 3),
            ([3, 0, 2, 0, 4], 7),
            ([4, 2, 0, 3, 2, 5], 9),
            ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ]

        for heights, expected in cases:
            with self.subTest(heights=heights):
                self.assertEqual(trap(heights), expected)

    def test_invalid_heights(self):
        for heights in ([1, -1, 2], [1, 1.5, 2]):
            with self.subTest(heights=heights):
                with self.assertRaises(ValueError):
                    trap(heights)

    def test_input_parsing(self):
        self.assertEqual(parse_heights("3 0 2 0 4"), [3, 0, 2, 0, 4])
        self.assertEqual(parse_heights("3,0,2,0,4"), [3, 0, 2, 0, 4])
        self.assertEqual(parse_heights("3，0，2"), [3, 0, 2])


if __name__ == "__main__":
    unittest.main()