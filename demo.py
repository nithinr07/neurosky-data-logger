from NeuroSkyPy.NeuroSkyPy import NeuroSkyPy
from time import sleep
import os

os.system("sudo rfcomm connect /dev/rfcomm0 C4:64:E3:E6:E3:7D 1 &")
sleep(3)
neuropy = NeuroSkyPy("/dev/rfcomm0")
neuropy.start()
while(True):
    #neuropy.start()
    print("Attention = ", neuropy.attention)
    print("Loose Contact = ", neuropy.poorSignal)
    print("Meditation = ", neuropy.meditation)
    print()
    sleep(0.2) # Don't eat the CPU cycles
