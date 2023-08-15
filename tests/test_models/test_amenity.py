#!/usr/bin/env python3
"""
testing module for the Amenity class
"""
import unittest
from models.amenity import Amenity


class TestAmenityClass(unittest.TestCase):
    """
    A unittest class to test our `Amenity class`
    """
    def setUp(self):
        """
        sets up the configuration for each test case
        """
        self.amenity = Amenity()

    def test_attributes(self):
        """
        tests of the Amenity class has the required atrributes
        """
        self.assertIsNotNone(self.amenity.name)

