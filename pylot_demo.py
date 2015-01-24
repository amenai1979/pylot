#!/usr/bin/python3
#Demonstrates the use of the pylot classes. May require python 3
#To execute from a commandline: python3 pylot_demo.py
__author__ = 'Alexandre Menai'
from bin.aircraft import *
if __name__=="__main__":
    print("Welcome to pylot! please contribute: https://github.com/amenai1979/pylot")
    avion1=Aircraft("PA38", "Piper",1670,"N9182A")
    print(avion1)
    avion1.set_balEnvelope(1000,1260,avion1.max_weight,72.4,73.5,78.5)
    print("The airplane's weight and balance envelope is (in,Lbs): {}".format(avion1.balEnvelope.points))
    if avion1.in_envelope((77,1650)):
        print("point {} is in weight and balance envelope".format("77 inches, 1650 Lbs"))
    if not avion1.in_envelope((71,1671)):
        print("point {} is NOT in weight and balance envelope, NO GO!!!".format("71 inches, 1671 Lbs"))