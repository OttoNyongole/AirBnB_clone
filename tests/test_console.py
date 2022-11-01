#!/usr/bin/python3
"""Test module for console""""

import unittest
import console
import inspect

HBNBCommand = console.HBNBCommand


class TestConsoleDocs(unittest.TestCase):
    """
    class for testing console documandation
    """

    def test_console_module_docstring(self):
        """docstring test for console module"""
        self.assertIsNot(console.__doc__, None,
                        "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """ Test for the HBNBCommand docstring"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                        "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")

