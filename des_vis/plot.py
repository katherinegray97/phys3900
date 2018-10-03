#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 12:28:31 2018

@author: katiegray
"""

import time
import numpy as np
import os, os.path
import sys
from survey import Survey
from camera import Camera
import vispy.scene
from vispy.scene import visuals
import imageio
import pickle
import matplotlib.pyplot as plt
from vispy.color import Colormap


def main():
    """
    Creates Survey and Camera classes, calls the plotting function
    """

    # Instantiate classes
    des = Survey(ras = data[:, 0], decs = data[:, 1], zs = data[:, 6], colour_diff = data[:,2] - data[:,3])
    cam = Camera(des)

    if (library is "vispy"):
        vispy_plot(des, cam)
    else:
        matplotlib_plot(des, cam)



def vispy_plot(des, cam):
    """
    Creates an animation saved to outputs/vispy_animation.gif using the VisPy
    plotting library
    """

    points = np.zeros((des.length, 3))

    canvas = vispy.scene.SceneCanvas()
    view = canvas.central_widget.add_view()
    scatter = visuals.Markers()
    scatter.set_data(points)
    view.add(scatter)

    # Camera controls
    view.camera = 'panzoom'
    view.camera.center = (0,0,0)
    view.camera.fov = cam.fov
    view.camera.set_range(x=(-0.5,0.5), y =(-0.5,0.5))

    # Colour map for points
    cm = Colormap(['b','b','w','r','r'],
                  controls = [0.0, des.mean-des.std, des.mean, des.mean + des.std, 1.0],
                  interpolation='linear')


    writer = imageio.get_writer('outputs/vispy_animation.gif')
    for i in range(frames):

        # Change this translation for a different fly-though path
        cam.translate(0.001,0,0,0,0)
        points[:,0] = cam.proj_x()
        points[:,1] = cam.proj_y()

        scatter.set_data(points, edge_color=None, face_color=cm[des.colour_diff], size=5*des.size)

        im = canvas.render()
        writer.append_data(im)

    writer.close()


def matplotlib_plot(des, cam):
    """
    Creates an animation saved to outputs/matplotlib_animation.gif
    using the Matplotlib plotting library
    """

    # Create 2D Matplotlib figure and axes
    fig, ax = plt.subplots(1, 1, figsize=(19.2, 10.8))

    # Remove subplot padding
    fig.subplots_adjust(left=0, bottom=0, right=1, top=1)

    fig.canvas.draw()

    for i in range(frames):

        # Change this translation for a different fly-though path
        cam.translate(0.001, 0, 0, 0, 0)

        ax.clear()
        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 1)

        ax.scatter(cam.proj_x(), cam.proj_y(), s=5*des.size)

        plt.draw()

        # Save to file
        name_out = "matplotlib_animation"
        fig.savefig("outputs/" + name_out + "{0:0=3d}".format(i), dpi = 100)

    # Convert to mp4 using ffmpeg
    os.system("./ffmpeg.sh " + name_out + " " + name_out )



if __name__ == "__main__":
    start = time.time()

    # Default program settings
    global library, fraction, frames
    library = "vispy"
    fraction =5
    frames = 20

    # Command line args
    if(len(sys.argv) > 1 and len(sys.argv) is not 4):
        print("Please enter the program settings: \n"+
              "1. an appropriate choice of plotting library - 'vispy' or 'matplotlib'\n"+
              "2. An integer to divde the dataset by for quick plotting of a random subset of data\n"+
              "3. An integer number of frames to plot")
        exit()
    elif (len(sys.argv) > 1):
        library, fraction, frames = sys.argv[1], sys.argv[2], sys.argv[3]

    print("Plotting", frames, "frames using", library,"with a " + str(fraction) + "th of the dataset.")


    # Load data
    fp = open("data/full_data", mode = "rb")
    data = pickle.load(fp)
    fp.close()

    # Truncate data
    n = len(data)//fraction
    data = data[0:n, :]

    main()

    print("Plotted", str(n), "points in", str(round(time.time() - start, 2)), "secs.")




