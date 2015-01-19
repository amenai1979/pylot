#!/usr/bin/python
import unittest
from bin.aircraft import Aircraft
class TestInit(unittest.TestCase):
    """test for initiliazing an Aircraft object"""
    def setUp(self):
        self.avion1=Aircraft("PA28", "Piper",2450,"N6910J")
    def test_init(self):
        self.assertEqual(self.avion1.make,"Piper")
        self.assertEqual(self.avion1.model,"PA28")
#now run the tests
unittest.main()