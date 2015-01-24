#!/usr/bin/python
__author__ = 'Alexandre Menai'
import unittest
from bin.aircraft import Aircraft
class TestAircraft(unittest.TestCase):
    """test for the an Aircraft object"""
    def setUp(self):
        self.avion1=Aircraft("PA38", "Piper",1670,"N9182A")
        self.avion1.set_balEnvelope(1000,1260,self.avion1.max_weight,72.4,73.5,78.5)
        self.point=(77,1650)
    def testInit(self):
        self.assertEqual(self.avion1.make,"Piper")
        self.assertEqual(self.avion1.model,"PA38")
        self.assertEqual(self.avion1.max_weight,1670)
        self.assertEqual(self.avion1.tail_number,"N9182A")
    def testBalEnvelope(self):
        self.assertEqual(self.avion1.balEnvelope.points, ((72.4, 1000), (72.4, 1260), (73.5, 1670), (78.5, 1670), (78.5, 1000)))
    def testWeightBalPoint(self):
        self.assertEqual(self.avion1.in_envelope(self.point),True)
        self.assertEqual(self.avion1.in_envelope((77,1671)),False)
        self.assertEqual(self.avion1.in_envelope((71,1671)),False)
        self.assertEqual(self.avion1.in_envelope((71,1650)),False)
#now run the tests
if __name__ == '__main__':
    unittest.main()