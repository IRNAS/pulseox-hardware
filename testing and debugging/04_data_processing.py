# -*- coding: utf-8 -*-
"""
Created on 2017 Sep 19
LAST UPDATE: 2017 Oct 16
Author: Luka Banovic (banovic@irnas.eu)

This script enables you to load the logged data from your GliaX pulse oximeter. It can be used either for debugging or for firmware development.

fs = 100 samples/second
fc = 3.3Hz - the heart beats up to 200bpm can be detected

A series of values in one row are:
  
  - timestamp ('ts')
  - raw IR value ('raw_ir)
  - dc filtered IR ignal ('dc_ir')
  - mean filtered IR signal ('mean_ir')
  - low pass filtered IR signal ('butt_ir')
  - dc filtered RED signal (dc_red)
  - raw orange signal (raw_orange)
  - raw yellow signal (raw_yellow)
  - normalised IR signal (norm_ir)
  - normalised RED signal (norm_red)
  - low pass filtered normalised IR signal (butt_norm_ir)
  - low pass filtered normalised RED signal (butt_norm_red)
  - ratio between IR and red ('ratio')
  - ambient light ('ambient')
  
"""


import os
os.chdir(r'working directory')			# change the working directory

import pandas
import numpy as np
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt

def load_dataset(filename):
    return pandas.read_csv(
        filename,
        header=None,
        names=['ts', 'raw_ir', 'dc_ir', 'mean_ir', 'butt_ir', 'dc_red','raw_orange','raw_yellow','norm_ir','norm_red','butt_norm_ir','butt_norm_red','ratio','ambient'])
        
        
def butter_lowpass(cut, fs, order=5):
  """ This function returns filter parameters for 5th order butterworth low pass filter with cutoff frequency 'cut'."""
    nyq = 0.5 * fs
    cut = cut / nyq
    b, a = butter(order, [cut], btype='low')
    return b, a

def butter_lowpass_filter(data, cut, fs, order=5):
  """ This function filters the 'data' signal and returns a filtered signal 'y' at a cutoff frequency 'cut'."""
    b, a = butter_lowpass(cut, fs, order=order)
    y = filtfilt(b, a, data)
    return y
    
    
class PeakDetector(object):
  """
  This function does the trough detection on signal.
  """
    def __init__(self, threshold):
        self.threshold = threshold
        self.previous_value = None
        self.state = 'idle'

    def push(self, value):
        if self.state == 'idle':
            if value <= self.threshold:
                self.state = 'rising'
        elif self.state == 'rising':
            if value < self.previous_value:
                pass
            else:
                self.state = 'falling'
                return True
        elif self.state == 'falling':
            if value > self.threshold:
                self.state = 'idle'

        self.previous_value = value
        return False    

"""======================================================================="""

"""
LOAD DATA
"""
        
data = load_dataset('InsertLogFile.txt')			# insert the name of your log file, including the .txt suffix

time = data['ts']
time = data['ts'] - data['ts'][0]
time = time/100

"""
Extract the data from the loaded dataset and create variables.
"""

raw_ir = data['raw_ir']
dc_ir = data['dc_ir']
mean_ir = data['mean_ir']
butt_ir = data['butt_ir']
dc_red = data['dc_red']
raw_orange = data['raw_orange']
raw_yellow = data['raw_yellow']
norm_red = data['norm_red']
norm_i = data['norm_ir']
b_n_red = data['butt_norm_red']
b_n_ir = data['butt_norm_ir']
ratio = data['ratio']

"""
LOW PASS FILTERRING
"""

raw_ir_ftd = butter_lowpass_filter(raw_ir, 3.3, 100, order=2)
dc_ir_ftd = butter_lowpass_filter(dc_ir, 3.3, 100, order=2)
mean_ir_ftd = butter_lowpass_filter(mean_ir, 3.3, 100, order=2)
dc_red_ftd = butter_lowpass_filter(dc_red, 3.3, 100, order=2)
raw_orange_ftd = butter_lowpass_filter(raw_orange, 3.3, 100, order=2)
raw_yellow_ftd = butter_lowpass_filter(raw_yellow, 3.3, 100, order=2)


"""
PEAK DETECTION
"""
detector = PeakDetector(threshold=0)
peaks = [detector.push(x) for x in dc_ir_ftd]
peaks = np.asarray(peaks)

item = True
peaks = np.where(peaks == item)
peaks = peaks[0]



