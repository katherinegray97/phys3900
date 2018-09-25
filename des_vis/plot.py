#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 12:28:31 2018

@author: katiegray
"""

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

    # Truncate data
    n = len(data)//10
    print(n)
    data = data[0:n, :]
    print("Truncated " + str(time.time()- start))

    # Instantiate classes
    # Find max r in survey, for setting threshold
    # print("MAX: " + str(np.amax(des._get_r())))
    des = Survey(data[:, 0], data[:, 1], data[:, 2], threshold = 0.9)
    cam = Camera(des)

    vispy_plot(des, cam)
    #matplotlib_plot(des,cam)

    print(str(n) + " points executed in: " + str(round(time.time() - start, 2)) + "secs")

def vispy_plot(des, cam):
    points = np.zeros((des.length, 2))
    canvas = vispy.scene.SceneCanvas()
    view = canvas.central_widget.add_view()

    scatter = visuals.Markers()
    scatter.set_data(points)
    view.add(scatter)

    view.camera = 'panzoom'
    view.camera.center = (0,0,0)
    view.camera.fov = 70
    view.camera.azimuth = 0
    view.camera.elevation = 0
    view.camera.distance = 0

    writer = imageio.get_writer('outputs/vispy_animation.gif')
    for i in range(20):
        cam.translate(0.001,0.0001,0,0,0)
        points[:,0] = cam.proj_x()
        points[:,1] = cam.proj_y()
        scatter.set_data(points, edge_color=None, face_color=ColorArray(des.colours), size=3*des.size)
        #scatter.set_data(points, edge_width=None, edge_width_rel=0.5, edge_color='red', face_color="white", size=20*des.size)
        im = canvas.render()
        writer.append_data(im)
    writer.close()


def matplotlib_plot(des, cam):
    print("Matplotlib function called " + str(time.time() - start))
    # Create 2D Matplotlib figure and axes
    fig, ax = plt.subplots(1, 1, figsize=(19.2, 10.8))

    # Remove subplot padding
    fig.subplots_adjust(left=0, bottom=0, right=1, top=1)

    fig.canvas.draw()

    ### Observer moves out - set to 100 for a nice video
    for i in range(0, 20):
        print("start " + str(time.time() - start))
        ax.clear()
        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 1)

        ax.scatter(cam.proj_x(), cam.proj_y(), c=des.colours, s=100*des.size)
        print("scattered " + str(time.time() - start))

        plt.draw()
        print("drawn " + str(time.time() - start))

        #save to file
        name_out = "refactored"
        fig.savefig("outputs/" + name_out + "{0:0=3d}".format(i), dpi = 100)


        print("saved " + str(time.time() - start))


        if (i < 15):
            cam.translate(0, 0, 0, 0.01, 0.01)
        elif(i < 20):
            cam.translate(0.001, 0, 0, 0.01, 0.01)
        else:
            cam.translate(0.001, 0, 0, 0, 0)

#        plt.cla()
        print(i)
    os.system("./ffmpeg.sh " + name_out + " "+ name_out )



if __name__ == "__main__":
    start = time.time()
    main()



