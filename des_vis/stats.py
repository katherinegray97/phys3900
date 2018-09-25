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
    # Delete old results files
    mypath = "outputs"
    for root, dirs, files in os.walk(mypath):
        for file in files:
            os.remove(os.path.join(root, file))

    # Load data
    fp= open("data/DESdata", mode = "rb")
    data = pickle.load(fp)
    fp.close()

    print("Loaded " + str(time.time() - start))


if __name__ == "__main__":
    main()
