from kallepaket.kalle import Kalle
from kallepaket.utils import kontrollera_längden_på_namnet
import unittest


class TestKalle(unittest.TestCase):
    
    def setUp(self):
        self.kalle = Kalle('kalle', 'anka')
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_capitalize_surename(self):
        self.assertEqual(self.kalle.förnamn, 'Kalle')

    def test_capitalize_familyname(self):
        self.assertEqual(self.kalle.efternamn, 'Anka')

class TestKontrolleraLängdenPåNamnet(unittest.TestCase):

    def test_incorrect_len_string(self):
        with self.assertRaises(ValueError):
            kontrollera_längden_på_namnet('h')
            kontrollera_längden_på_namnet('')

    def test_correct_len_string(self):
        val = kontrollera_längden_på_namnet('Kalle')
        self.assertEqual(val, 5)

if __name__ == '__main__':
    unittest.main()