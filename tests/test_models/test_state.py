#!/usr/bin/env python3
"""
testing module for the State class
"""
import unittest
from models.state import State


class TestStateClass(unittest.TestCase):
    """
    A unittest class to test our `State class`
    """
    def setUp(self):
        """
        sets up the configuration for each test case
        """
        self.state = State()

    def test_name(self):
        """
        tests if the State class has the name atrribute
        """
        self.assertIsNotNone(self.state.name)

