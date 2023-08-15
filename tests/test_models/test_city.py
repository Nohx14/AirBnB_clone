#!/usr/bin/env python3
"""
testing module for the City class
"""
import unittest
from models.city import City


class TestCityClass(unittest.TestCase):
    """
    A unittest class to test our `City class`
    """
    def setUp(self):
        """
        sets up the configuration for each test case
        """
        self.city = City()

    def test_attributes(self):
        """
        tests if the City class has the neccessary attributes
        """
        self.assertIsNotNone(self.city.state_id)
        self.assertIsNotNone(self.city.name)
