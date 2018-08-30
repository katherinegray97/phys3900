import numpy as np

import matplotlib.pyplot as plt

import time
import os, re, os.path
from plot_data import PlotData
from translator import Translator
import subprocess
if __name__ == "__main__":

    start= time.time()
    # Import data
    data = np.load("des_thinned.npy")

    # Clean data, remove nans
    data = data[~np.isnan(data).any(axis=1)]

    # Truncate, for testing
    np.random.shuffle(data)
    numpoints = len(data)//100
    des = PlotData(data[0:numpoints, 0], data[0:numpoints, 1],
                   data[0:numpoints, 2])

    # Delete files
    mypath = "outputs"
    for root, dirs, files in os.walk(mypath):
        for file in files:
            os.remove(os.path.join(root, file))

    # Viewport width and height
    v_x, v_y = 1920, 1080
    aspect = v_x / v_y  # Python 3 required
    fov = 70  # Camera FOV
    fov_w = 0.5 * 70 * np.pi / 180
    fov_h = fov_w / aspect

    translator = Translator(des)


    #rotate so that points are in front of camera
    fig, ax = plt.subplots(1, 1, figsize=(19.2, 10.8))
    # removes subplot padding
    fig.subplots_adjust(left=0, bottom=0, right=1, top=1)
    count =0;

    ### Observer moves out - set to 100 for a nice video
    for i in range(0, 100):

        proj_x = np.arctan2(translator.plot_data.close_y, translator.plot_data.close_x) / np.tan(fov_w)
        proj_y = np.arctan2(translator.plot_data.close_z,  translator.plot_data.close_x) / np.tan(fov_h)

        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 1)
        ax.scatter(proj_x, proj_y, c=translator.plot_data.close_alpha, s=100*translator.plot_data.close_size)

        #save to file
        name_out = "refactored"
        name = "outputs/"+name_out+ "{0:0=3d}".format(i)

        fig.savefig(name, dpi = 100)


        if (count < 15):
            translator.translate(0, 0, 0, 0.01, 0.01)
        elif(count <20):
            translator.translate(0.001, 0, 0, 0.01, 0.01)
        else:
            translator.translate(0.001, 0, 0, 0, 0)

        plt.cla()
        count+=1
        print(i)


    print(str(numpoints) + " points in " + str(i+1) + " plots executed in: " + str(round(time.time() - start, 2)) + "secs")
    print("ffmpegging")
    os.system("./ffmpeg.sh " + name_out + " "+ name_out )
    print("Done!")