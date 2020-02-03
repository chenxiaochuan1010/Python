import unittest
from city_functions import formmated_city_country_name

class CityCountryTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Do 'Santiago, Chile' results in correct string?"""
        formatted_name = formmated_city_country_name('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')

    def test_city_country_population(self):
        """Do 'Santiago, Chile - population 5000000' results correctly"""
        formatted_name = formmated_city_country_name(
                'santiago', 'chile', 5000000)
        self.assertEqual
                formatted_name, 'Santiago, Chile - population 5000000')

unittest.main()
