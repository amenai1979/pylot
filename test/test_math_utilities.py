#!/usr/bin/python
__author__ = 'Alexandre Menai'

import unittest
from bin.math_utilities import *

class TestPolygon(unittest.TestCase):
    def setUp(self):
        self.mysquare=Polygon((0,0),(0,1),(1,1),(1,0))
        self.point=(0.25,0.25)
    def test_init(self):
        self.assertEqual(self.mysquare.points,((0,0),(0,1),(1,1),(1,0)))
    def test_point_inside(self):
        self.mysquare.point_inside_polygon(self.point[0],self.point[1])

if __name__ == '__main__':
    unittest.main()