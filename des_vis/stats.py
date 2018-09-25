#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 20:41:20 2018

@author: katiegray
"""
import time
import numpy as np
import os, os.path
from survey import Survey
from camera import Camera
import vispy.scene
from vispy.scene import visuals
import imageio
import pickle
from vispy.color import ColorArray
import matplotlib.pyplot as plt


def main():
    # Load data
    fp= open("data/DESdata", mode = "rb")
    data = pickle.load(fp)
    fp.close()

    green_red_diff = data[:,2] - data[:,3]
    print(min(green_red_diff))
    print(max(green_red_diff))
    # the histogram of the data
    n, bins, patches = plt.hist(green_red_diff, 50, density=True, facecolor='g', alpha=0.75)
    fig, ax = plt.subplots(1,1)
    plt.xlabel('Green-Red')
    plt.ylabel('Probability')
    plt.title('Histogram of Green-Red')
    plt.grid(True)
    fig.savefig("outputs/hist")
    plt.show()



if __name__ == "__main__":
    main()