
from NeuroSkyPy.NeuroSkyPy import NeuroSkyPy
from time import sleep
from itertools import count
import os
import sys
from matplotlib.animation import FuncAnimation  
import matplotlib.pyplot as plt  
import numpy as np 
import csv
import signal
import time

class NeuroSkyLogger():

    def __init__(self, comm_port, fs, folderPath):
        self.fs = fs
        self.dt = 1/fs
        self.comm_port = comm_port
        self.folderPath = folderPath
        
    def setupCSV(self):
        self.fieldnames = ["time", "attention", "contact"]
        file_count = sum(len(files) for _, _, files in os.walk(os.path.join(self.folderPath, "data")))
        self.filePath = os.path.join(os.path.join(self.folderPath, "data", "data_{}.csv".format(file_count + 1)))

        with open(self.filePath, 'w+') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
            csv_writer.writeheader()

    #Countdown to start game/data collection
    def countDown(self):
        print("Start the game at the end of countdown.....")
        seconds = 10
        while(seconds > 0):
            print(seconds)
            seconds -= 1
            sleep(1)
        print("START")

    #collect data from NeuroSky
    def NeuroskyLogger(self):

        neuropy = NeuroSkyPy(self.comm_port)
        neuropy.start()

        sample_count = 0
        
        count_down = False
        start = time.time()
        while(True):
            
            # t = sample_count * self.dt
            attn = neuropy.attention
            contact = neuropy.poorSignal
            t = time.time() - start

            # print(t)
            #wait for 20 seconds for neurosky to start reliable transmission
            if t > 20:
                if count_down:
                    with open(self.filePath, 'a', newline='') as csv_file:
                        csv_writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)

                        info = {
                            "time": t,
                            "attention": attn,
                            "contact": contact
                        }
                        csv_writer.writerow(info)

                else:
                    self.countDown()
                    count_down = True
            else:
                print("Attention = ", neuropy.attention)
                print("Loose Contact = ", neuropy.poorSignal)
            sleep(self.dt)
            sample_count += 1

    #Data collection
    def collectData(self):

        self.setupCSV()
        self.NeuroskyLogger()


if __name__ == "__main__":

    comm_port = "COM5"
    fs = 5 #Hz
    folderPath = os.path.join("D:", "Semester8", "RE", "experiments", "neurosky_testing")

    data_logger = NeuroSkyLogger(comm_port, fs, folderPath)
    data_logger.collectData()

