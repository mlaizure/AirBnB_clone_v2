#!/usr/bin/python3
"""unittests for console"""
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(TestCase):
    """tests the console"""
    def test_do_create(self):
        """test do_create"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create PoorUnfortunateSouls")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
