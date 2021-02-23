
from NeuroSkyPy.NeuroSkyPy import NeuroSkyPy
from time import sleep
import os
import sys


neuropy = NeuroSkyPy("COM5", 57600)
neuropy.start()
while(True):

    print("Attention = ", neuropy.attention)
    print("Loose Contact = ", neuropy.poorSignal)
    print("Meditation = ", neuropy.meditation)
    print()
    sleep(0.2) # Don't eat the CPU cycles