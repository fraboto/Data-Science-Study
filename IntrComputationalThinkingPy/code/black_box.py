import unittest

def suma(a, b):
    return a + b

class ClassBlackBoxTest(unittest.TestCase):

    def test_sum_positives(self):
        num_1 = 10
        num_2 = 5

        result = suma(num_1, num_2)

        self.assertEqual(result, 15)

    def test_sum_negatives(self):
        num_1 = -5
        num_2 = -6


        result = suma(num_1, num_2)

        self.assertEqual(result, -11)

if __name__ == '__main__':
    unittest.main()