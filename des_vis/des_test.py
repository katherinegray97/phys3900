import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
import os, re, os.path
from plot_data import PlotData
from translator import Translator



if __name__ == "__main__":
    start= time.time()
    # Import data
    data = np.load("des_thinned.npy")

    # Clean data, remove nans
    data = data[~np.isnan(data).any(axis=1)]

    # Truncate, for testing
    numpoints = 500 # len(data)
    des = PlotData(data[0:numpoints, 0], data[0:numpoints, 1],
                   data[0:numpoints, 2])

    translator = Translator(des)
    # Delete files
    mypath = "outputs"
    for root, dirs, files in os.walk(mypath):
        for file in files:
            os.remove(os.path.join(root, file))

    ######ROTATE
    for i in range(1, 35):
        fig = plt.figure(figsize=(2,2), dpi=192, frameon=False)

        # removes subplot padding
        fig.subplots_adjust(left=0, bottom=0, right=1, top=1)

        ax = fig.add_subplot(111, projection='3d')

        # axis off, black background
        ax.set_axis_off()
        ax.patch.set_facecolor('black')

        #set camera to be looking down x axis (y increasing on left)
        ax.view_init(elev=0,
                     azim=180)

        ax.set_xlim(0, 3)
        ax.set_ylim(-0.25,0.25)
        ax.set_zlim(0, 0.15)

        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')

        ax.scatter(translator.plot_data.close_x, translator.plot_data.close_y,
                   translator.plot_data.close_z, marker="*",
                   c=translator.plot_data.alpha)
        name_out = "outputs/turn" + "{0:0=3d}".format(i)

        #save to file
        fig.savefig(name_out, dpi=192,  pad_inches=0)

        #translate
        translator.translate(0, 0, 0,np.pi/10,0)
        plt.close("all")

    print(str(numpoints) + " points executed in: " + str(round(time.time()-start,2)) + "secs")






