#!/usr/bin/python3

"""
    Defines a class City.
"""


from models.city import City
import unittest
import models
import os


class TestCity(unittest.TestCase):
    """Represent a City test."""

    def test_docstring(self):
        """Test docstring for the module and the class"""

        self.assertIsNotNone(
            models.city.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(City.__doc__, "No docstring in the class")

    def test_permissions_file(self):
        """Test File city.py permissions"""

        test_file = os.access("models/city.py", os.R_OK)
        self.assertTrue(test_file, "Read permissions")
        test_file = os.access("models/city.py", os.W_OK)
        self.assertTrue(test_file, "Write Permissions")
        test_file = os.access("models/city.py", os.X_OK)
        self.assertTrue(test_file, "Execute permissions")

    def test_type_object(self):
        """Test type object of City"""

        city = City()
        self.assertEqual(
            str(type(city)),
            "<class 'models.city.City'>")
        self.assertIsInstance(city, City)


if __name__ == "__main__":
    unittest.main()
