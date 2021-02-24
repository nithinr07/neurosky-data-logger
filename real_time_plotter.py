from time import sleep
import os
import sys
from matplotlib.animation import FuncAnimation  
import matplotlib.pyplot as plt  
import numpy as np 
import csv
import pandas as pd

attention = []
time = []

folderPath = os.path.join("D:", "Semester8", "RE", "experiments", "neurosky_testing")
file_count = sum(len(files) for _, _, files in os.walk(os.path.join(folderPath, "data")))
filePath = os.path.join(os.path.join(folderPath, "data", "data_{}.csv".format(file_count)))

def animate(i):
    data = pd.read_csv(filePath)
    time = data['time']
    attention = data['attention']
    bs = data['blink strength']
    meditation = data['meditation']

    plt.cla()
    att_signal = plt.plot(time, attention)
    med_signal = plt.plot(time, meditation)
    plt.title('Attention signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend(['Attention', 'Meditation'], loc = 'upper right')
    # plt.savefig(os.path.join(folderPath, "graphs", "graph_{}.csv".format(file_count)))

plt_real_time = FuncAnimation(plt.gcf(), animate, 1)
plt.show()
# plt.savefig(os.path.join(folderPath, "graphs", "graph_{}.csv".format(file_count)))