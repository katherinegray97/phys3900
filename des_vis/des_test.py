import numpy as np

import matplotlib.pyplot as plt

import time
import os, os.path
from survey import Survey
from camera import Camera

if __name__ == "__main__":

    start = time.time()

    # Delete old results files
    mypath = "outputs"
    for root, dirs, files in os.walk(mypath):
        for file in files:
            os.remove(os.path.join(root, file))

    # Import data
    data = np.load("des_thinned.npy")

    # Clean data, remove nans
    data = data[~np.isnan(data).any(axis=1)]

    # Shuffle and truncate, for testing
    np.random.shuffle(data)
    n = len(data)//100
    data = data[0:n, :]


    # Instantiate classes
    des = Survey(data[:, 0], data[:, 1], data[:, 2])
    cam = Camera(des)

    # Create 2D Matplotlib figure and axes
    fig, ax = plt.subplots(1, 1, figsize=(19.2, 10.8))

    # Remove subplot padding
    fig.subplots_adjust(left=0, bottom=0, right=1, top=1)


    ### Observer moves out - set to 100 for a nice video
    for i in range(0, 1):
        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 1)
        ax.scatter(cam.get_points_x(), cam.get_points_y()) #c=des.alpha, s=100*des.size

        #save to file
        name_out = "refactored"
        fig.savefig("outputs/" + name_out + "{0:0=3d}".format(i), dpi = 100)

        if (i < 15):
            cam.translate(0, 0, 0, 0.01, 0.01)
        elif(i < 20):
            cam.translate(0.001, 0, 0, 0.01, 0.01)
        else:
            cam.translate(0.001, 0, 0, 0, 0)

        plt.cla()

        print(i)



    print(str(n) + " points in " + str(i+1) + " plots executed in: " + str(round(time.time() - start, 2)) + "secs")
#    print("ffmpegging")
#    os.system("./ffmpeg.sh " + name_out + " "+ name_out )
#    print("Done!")