import unittest
from app import prepare_order


class TestInputType(unittest.TestCase):
    def test_type(self):
        self.assertTrue(prepare_order(2.0), None)
        self.assertTrue(prepare_order(True), None)
        self.assertTrue(prepare_order("2"), True)


class TestOrdersQuantity(unittest.TestCase):
    def test_small_boxes(self):
        small_cases = [1, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100]

        for case in small_cases:
            self.assertEqual(prepare_order(case)['small'], 1)

    def test_medium_boxes(self):
        medium_cases = [4, 6, 22, 31, 40, 49, 58, 67, 76, 85, 94]

        for case in medium_cases:
            self.assertEqual(prepare_order(case)['medium'], 1)

    def test_large_boxes(self):
        self.assertEqual(prepare_order(8)['large'], 1)
        self.assertEqual(prepare_order(20)['large'], 2)


if __name__ == '__main__':
    unittest.main()