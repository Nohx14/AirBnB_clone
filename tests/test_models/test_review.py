#!/usr/bin/env python3
"""
testing module for the Review class
"""
import unittest
from models.review import Review


class TestReviewClass(unittest.TestCase):
    """
    A unittest class to test our `Review class`
    """
    def setUp(self):
        """
        sets up the configuration for each test case
        """
        self.review = Review()

    def test_attributes(self):
        """
        verifies that the Review class has all the required attributes
        """
        self.assertIsNotNone(self.review.place_id)
        self.assertIsNotNone(self.review.user_id)
        self.assertIsNotNone(self.review.text)

