#!/usr/bin/env python3
"""
testing module for the Place class
"""
import unittest
from models.place import Place


class TestPlaceClass(unittest.TestCase):
    """
    A unittest class to test our `Place class`
    """
    def setUp(self):
        """
        sets up the configuration for each test case
        """
        self.place = Place()

    def test_attributes(self):
        """
        verifies that the Place class has the required attributes
        """
        self.assertIsNotNone(self.place.city_id)
        self.assertIsNotNone(self.place.user_id)
        self.assertIsNotNone(self.place.name)
        self.assertIsNotNone(self.place.description)
        self.assertIsNotNone(self.place.number_rooms)
        self.assertIsNotNone(self.place.number_bathrooms)
        self.assertIsNotNone(self.place.max_guest)
        self.assertIsNotNone(self.place.price_by_night)
        self.assertIsNotNone(self.place.latitude)
        self.assertIsNotNone(self.place.longitude)
        self.assertIsNotNone(self.place.amenity_ids)

