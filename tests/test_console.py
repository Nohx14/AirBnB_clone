#!/usr/bin/env python3
"""
module to test our application console
"""


import unittest
from unittest.mock import patch
from io import StringIO
import re
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """
    TestConsole:
        A class to test our console application
    """
    def test_start(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertTrue(re.match(r'[a-z0-9-+]', f.getvalue()))
