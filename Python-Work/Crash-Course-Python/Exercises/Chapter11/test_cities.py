import unittest
from city_functions import return_Location

class NamesTestCase(unittest.TestCase):
    def test_location(self):
        location = return_Location("London", "UK")
        self.assertEqual("London UK", location)

    def test_city_country_population(self):
        location = return_Location("London", "UK", str(20000))
        self.assertEqual("London UK - population 20000", location)

unittest.main()
