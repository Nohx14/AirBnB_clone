#!/usr/bin/env python3
"""
Unittest module to test the User class
"""
import unittest
from models import user
User = user.User


class TestUserClass(unittest.TestCase):
    """
    Tests the User Class
    """

    def setUp(self):
        """
        method called before each test
        """
        self.user = User()

    def test_email(self):
        """
        tests if the email is alocated for a user
        """
        self.assertIsNotNone(User.email)
        self.assertIsNotNone(self.user.email)

    def test_password(self):
        """
        tests if the password attribute of the
        User class is available
        """
        self.assertIsNotNone(User.password)
        self.assertIsNotNone(self.user.password)

    def test_first_name(self):
        """
        tests if tr first name of the User class
        is given and not empty
        """
        self.assertIsNotNone(self.user.first_name)

    def test_last_name(self):
        """
        tests if the User class has a last_name attribute
        """
        self.assertIsNotNone(User.last_name)
        self.assertIsNotNone(self.user.last_name)

    def test_documentation(self):
        """
        check if all functions and class and the module
        itself is documented
        """
        self.assertIsNotNone(user.__doc__)
        self.assertIsNotNone(User.__doc__)

