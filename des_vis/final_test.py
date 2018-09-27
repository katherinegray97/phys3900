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
from vispy.color import Colormap


def main():
    dataset = "fake"
    data = np.zeros((50, 3))
    data[:,0] = np.linspace(0,1,num = 50)
    data[:,1] = data[:,0]
    data[:,2] = -10000

#    des = Survey(data[:, 0], data[:, 1], data[:, 2], threshold = 0.9, xs = data[:, 0], ys = data[:, 1], true_zs = data[:, 2])
#
#    cam = Camera(des)
    start_x =0# -1
    start_y = 0#-0.2
    start_theta = np.pi/8
#    cam.translate(start_x,start_y,0,0,0)

    vispy_plot(des, cam, dataset, start_x, start_y, start_theta, data)
    #matplotlib_plot(des,cam)

    print(str(n) + " points executed in: " + str(round(time.time() - start, 2)) + "secs")

def vispy_plot(des, cam, dataset, start_x, start_y, start_theta, data):
    points = np.zeros((des.length, 3))
    canvas = vispy.scene.SceneCanvas()
    view = canvas.central_widget.add_view()
    print(data)
    scatter = visuals.Markers()
    scatter.set_data(points)
    view.add(scatter)

    view.camera = 'panzoom'
    view.camera.center = (0,0,0)
    view.camera.fov = 70
    view.camera.set_range(x=(0,1), y =(0,1))

    writer = imageio.get_writer('outputs/test.gif')
    max_i = 10
    for i in range(max_i):

        print(str(cam.x) + " " + str(cam.y)+ " " + str(cam.z))
        dx = -start_x*2/max_i
        dy = -start_y*2/max_i
        dphi = -start_theta*2/max_i

#        cam.translate(0.1,dy,0,0,dphi)

        points = data



        if(dataset =='full'):
            scatter.set_data(points, edge_color=None, face_color=cm[des.colour_diff], size=5*des.size)
            cm = Colormap(['r','r','w','b','b'], controls=[0.0,des.mean-des.std,des.mean,des.mean + des.std, 1.0], interpolation='linear')
        else:
            scatter.set_data(points, edge_color=None, face_color="r", size=50)

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
    for i in range(0, 1):

        if (i < 15):
            cam.translate(0, 0, 0, 0.01, 0.01)
        elif(i < 20):
            cam.translate(0.001, 0, 0, 0.01, 0.01)
        else:
            cam.translate(0.001, 0, 0, 0, 0)

        ax.clear()
        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 1)

        ax.scatter(cam.proj_x(), cam.proj_y(), c=des.colours, s=100*des.size)

        plt.draw()
        #save to file
        name_out = "refactored"
        fig.savefig("outputs/" + name_out + "{0:0=3d}".format(i), dpi = 100)

#        plt.cla()
        print(i)
    os.system("./ffmpeg.sh " + name_out + " "+ name_out )



if __name__ == "__main__":
    start = time.time()
    print("Start ", time.asctime(time.localtime(start)) )
    main()



