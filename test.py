from primes import is_prime
import unittest


class TestIsPrime(unittest.TestCase):

    def test_correct_prime_numbers(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(13))

    def test_positiv_non_prime_numbers(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(9))

    def test_negative_numbers(self):
        self.assertFalse(is_prime(-5))
        self.assertFalse(is_prime(-2))

    def test_large_prime_number(self):
        self.assertTrue(is_prime(7919))  # 7919 är ett primtal

if __name__ == '__main__':
    unittest.main()
