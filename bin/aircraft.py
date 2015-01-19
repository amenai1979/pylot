#!/usr/bin/python3
import math_utilities
class Aircraft:
    """An attempt to model an aircraft"""
    def __init__(self, model="PA38", make="Piper", max_weight=1670, tail_number="N9182A"):
        """Every aircraft has a
		    make : the aircraft make
		    model : the aircraft model
		    max_weight : the maximum take off weight
            tail_number : tail number
		"""
        self.max_weight = max_weight
        self.model = model
        self.make = make
        self.tail_number = tail_number
        self.enveloppe=[]
    def weight_ok(self, weight):
        """
        :param weight: the current weight of an aircraft instance
        :return: True if the weight is less or equal the configured max weight
        """
        if self.max_weight >= weight:
            return True
        else:
            return False
    def __repr__(self):
        """
        makes representig the main parameters easier to consume
        :return:
        """
        return 'make: {}, model {}, max tkoff weight: {}, tail number: {}'.format(self.make, self.model, self.max_weight, self.tail_number)
    def bal_envelope(self, mini_weight, maxi_weight, mini_cg, maxi_cg, mid_weight, mid_cg):
        """
        Allows defining the weight and balance envelope
        :param mini_weight: defines the minimal weight reference in the weight and balance chart of the aircraft
        :param maxi_weight: define the maximum weight reference in the weight and balance chart of the aircraft
        :param mini_cg: defines the minimum distance to the cg datum in the weight and balance chart of the aircraft
        :param maxi_cg: defines the minimum distance to the cg datum in the weight and balance chart of the aircraft
        :param mid_weight: defines the weight component of the point generally found on the north west of the weight and balance chart of the aircraft
        :param mid_cg: defines the cg distance component of the point generally found on the north west of the weight and balance chart of the aircraft
        :return:
        """
        self.envelope = [(mini_cg,mini_weight),(mini_cg,mid_weight),(mid_cg,maxi_weight), (maxi_cg,max_weight), (max_cg,mini_weight)]
    def in_envelope(self, point):
        """
        :param point: defines a calculated weight and balance point
        :return: True if a point is in the envelope false otherwise
        """
        return math_utilities.point_inside_polygon(point,self.envelope)
