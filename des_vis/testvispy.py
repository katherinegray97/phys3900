#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 07:58:12 2018

@author: katiegray
"""

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
    dataset = "full"

    # Load data
    if(dataset == "full"):
        fp = open("data/full_data", mode = "rb")
    else:
        fp = open("data/thin_data", mode = "rb")

    data = pickle.load(fp)
    fp.close()

    # Truncate data
    n = len(data)//100
    print(n)
    data = data[0:n, :]
    print("Truncated " +  str(round(time.time() - start, 2)) + " secs")

    # Instantiate classes
    # Find max r in survey, for setting threshold
    # print("MAX: " + str(np.amax(des._get_r())))

    if(dataset == "full"):
        des = Survey(data[:, 0], data[:, 1], data[:, 6], colour_diff = data[:,2] - data[:,3], threshold = 0.9)
    else:
        des = Survey(data[:, 0], data[:, 1], data[:, 2], threshold = 0.9)

    des = Survey(data[:, 0], data[:, 1], data[:, 2], threshold = 0.9)




    data = np.zeros((50, 3))
    data[:,0] = np.linspace(0,10,num = 50)
    data[:,1] = data[:,0]
    data[:,2] = -10000


    des = Survey(data[:, 0], data[:, 1], data[:, 2], threshold = 0.9, xs = data[:, 0], ys = data[:, 1], true_zs = data[:, 2])




    cam = Camera(des)
    start_x =0# -1
    start_y = 0#-0.2
    start_theta = np.pi/8
    cam.translate(start_x,start_y,0,0,0)

    points = np.zeros((des.length, 3))
    canvas = vispy.scene.SceneCanvas(bgcolor='w')
    view = canvas.central_widget.add_view()

    scatter = visuals.Markers()
    scatter.set_data(points)
    view.add(scatter)
    view.camera = 'panzoom'
    view.camera.center = (0,0,0)
    view.camera.fov = 70
    view.camera.set_range(x=(-10,10), y =(-10,10))
    print(view.camera.get_state())

    axis = visuals.XYZAxis(parent=view.scene)

    writer = imageio.get_writer('vispy_out/vispy_animation.gif')
    max_i = 16
    cam.translate(0,0,0,-np.pi/8,0)
    for i in range(max_i):

        print(str(cam.x) + " " + str(cam.y)+ " " + str(cam.z))
        cam.translate(0,0,0,np.pi/8,0)
        points[:,0] = des.xs
        points[:,1] = des.ys
        points[:,2] = des.zs


        scatter.set_data(points)

        im = canvas.render()
        writer.append_data(im)
    writer.close()



if __name__ == "__main__":
    start = time.time()
    print("Start ", time.asctime(time.localtime(start)) )
    main()



