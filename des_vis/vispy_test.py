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
from vispy import app

def main():


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
    n = len(data)//1000
    data = data[0:n, :]


    # Instantiate classes
    des = Survey(data[:, 0], data[:, 1], data[:, 2], threshold=0.5)
    cam = Camera(des)

    points = np.zeros((des.length, 3))
    points[:,0] = cam.proj_x()
    points[:,1] = cam.proj_y()

    canvas = vispy.scene.SceneCanvas(keys='interactive', show=True)
    view = canvas.central_widget.add_view()
    scatter = visuals.Markers()
    scatter.set_data(points, edge_color=None, face_color=des.colours, size=des.size)
    view.add(scatter)
    view.camera = 'panzoom'
    view.camera.center = (0,0,0)
    view.camera.fov = 70
    view.camera.azimuth = 0
    view.camera.elevation = 0
    view.camera.distance = 0

#    def update(ev):
#        cam.translate(0.01,0.01,0,0,0)
##        points[:,0] = des.xs
#        points[:,0] = cam.proj_x()
#        points[:,1] = cam.proj_y()
#        scatter.set_data(points, edge_color=None, face_color=(1, 1, 1, 1), size=10)


    timer = app.Timer()
#    timer.connect(update)
    timer.start(0)
    vispy.app.run()


if __name__ == "__main__":
    start = time.time()
    main()
    print(str(n) + " points in " + str(i+1) + " plots executed in: " + str(round(time.time() - start, 2)) + "secs")