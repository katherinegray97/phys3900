#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 20:41:20 2018

@author: katiegray
"""

import numpy as np
import pickle
import matplotlib.pyplot as plt

def main():
    # Load data
    fp= open("data/full_data", mode = "rb")
    data = pickle.load(fp)
    fp.close()

    green_red_diff = data[:,2] - data[:,3]
    average = np.mean(green_red_diff)

    print(average, average + 10)
    mask = (green_red_diff < (average + 10)) & (green_red_diff > (average - 10))
    data = data[mask]
    green_red_diff = data[:,2] - data[:,3]
    fig, ax = plt.subplots()

    ax.set_xlim(average - 10, average + 10)
    print(np.percentile(green_red_diff, [25, 50, 75]))
    print(green_red_diff.min(), green_red_diff.max())
    print(np.mean(green_red_diff), np.std(green_red_diff))

    # the histogram of the data
    n, bins, patches = plt.hist(data[:,6], bins=100000, density=True, facecolor='g', alpha=0.75)

    plt.xlabel('g-r [magnitudes]')
    plt.ylabel('Probability')
    plt.title('Difference in apparent magnitude through green and red filters')
    plt.grid(True)
    fig.savefig("outputs/hist")


if __name__ == "__main__":
    main()
