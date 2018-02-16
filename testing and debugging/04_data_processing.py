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
# -*- coding: utf-8 -*-
"""
Created on 2017 Nov 19 

@ author: Luka Banovic
@ email: banovic@irnas.eu
"""


import os
os.chdir(r'')			# insert the path to working directory
import pandas
import numpy as np
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt


def load_dataset(filename):
    """
	This function reads the data from a .txt file.
    """
    data = pandas.read_csv(filename, header=None, names=['ts', 'raw_ir', 'dc_ir', 'mean_ir', 'butt_ir', 'dc_red','raw_orange','raw_yellow','norm_ir','norm_red','butt_norm_ir','butt_norm_red','ratio','ambient','raw_red'])
    time = data['ts']
    time = data['ts'] - data['ts'][0]
    time = time/1000

    raw_ir = data['raw_ir']
    dc_ir = data['dc_ir']/100
    mean_ir = data['mean_ir']/100
    butt_ir = data['butt_ir']/100
    dc_red = data['dc_red']/100
    raw_orange = data['raw_orange']
    raw_yellow = data['raw_yellow']
    norm_red = data['norm_red']/100000
    norm_ir = data['norm_ir']/100000
    b_n_red = data['butt_norm_red']/100000
    b_n_ir = data['butt_norm_ir']/100000
    ratio = data['ratio']/100
    ambient = data['ambient']
    raw_red = data['raw_red']
    return time, raw_ir, dc_ir, mean_ir, butt_ir, dc_red, raw_orange, raw_yellow, norm_red, norm_ir, b_n_red, b_n_ir, ratio, ambient, raw_red
        
    
def butter_lowpass(cut, fs, order=2):
    nyq = 0.5 * fs
    cut = cut / nyq
    b, a = butter(order, [cut], btype='low')
    return b, a

def butter_lowpass_filter(data, cut, fs, order=2):
    b, a = butter_lowpass(cut, fs, order=order)
    y = filtfilt(b, a, data)
    return y

def butter_highpass(cut, fs, order=2):
    nyq = 0.5 * fs
    cut = cut / nyq
    b, a = butter(order, [cut], btype='high')
    return b, a

def butter_highpass_filter(data, cut, fs, order=2):
    b, a = butter_highpass(cut, fs, order=order)
    y = filtfilt(b, a, data)
    return y


class PeakDetector(object):
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


def trough_decection(signal, treshold):
    """
    """
    detector = PeakDetector(threshold=treshold)
    peaks = [detector.push(x) for x in signal]
    peaks = np.asarray(peaks)
    
    item = True
    peaks = np.where(peaks == item)
    peaks = peaks[0]
    return peaks

"""======================================================================="""   
filename = 'MyPulseoxData.txt'        # insert the filename of the file where your data is stored

# here, time, raw_ir, dc_ir, dc_red and raw_red data are collected. Should you wish to inspect any other set of data,
# replace the respective "_" with the variable name found in 'load_dataset' function.
time, raw_ir, dc_ir, _, _, dc_red, _, _, _, _, _, _, _, _, raw_red = load_dataset(filename)

dc_ir_ftd = butter_lowpass_filter(dc_ir, 3.3, 100, order=1)
peaks = trough_decection(dc_ir_ftd, treshold=0)

