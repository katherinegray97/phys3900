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
from moviepy.editor import VideoClip
from vispy.gloo.util import _screenshot

import imageio
from vispy.gloo.util import _screenshot
from vispy.color.color_array import ColorArray


def main():
    # Delete old results files
    mypath = "outputs"
    for root, dirs, files in os.walk(mypath):
        for file in files:
            os.remove(os.path.join(root, file))

    # Import data
    data = np.load("data/full_des.npy")

    # Clean data, remove nans
    data = data[~np.isnan(data).any(axis=1)]

    # Shuffle and truncate, for testing
    np.random.shuffle(data)
    n = len(data)//100
    data = data[0:n, :]

    # Instantiate classes
    des = Survey(data[:, 0], data[:, 1], data[:, 2])
    cam = Camera(des)

    points = np.zeros((des.length, 3))
    points[:,0] = cam.proj_x()
    points[:,1] = cam.proj_y()

    canvas = vispy.scene.SceneCanvas()
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

#    def make_frame(t):
#        cam.translate(0.01,0.0001,0,0,0)
#        points[:,0] = cam.proj_x()
#        points[:,1] = cam.proj_y()
#        scatter.set_data(points, edge_color=None, face_color=des.colours, size=des.size)
#        canvas.on_draw('points') # Update the image on Vispy's canvas
#        return _screenshot((0,0,canvas.size[0],canvas.size[1]))[:,:,:3]
#
#    animation = VideoClip(make_frame, duration=1).resize(width=350)
#    animation.write_gif('sinc_vispy.gif', fps=20, opt='OptimizePlus')

#    def update(ev):
#        cam.translate(0.01,0.0001,0,0,0)
#        points[:,0] = cam.proj_x()
#        points[:,1] = cam.proj_y()
#        alpha = 1.0 / n ** 0.08
#        color = np.random.uniform(0.1, 0.9, (3,))
#        scatter.set_data(points, edge_color=None, face_color=des.colours, size=des.size)
#        img = canvas.render()
#        io.write_png("outputs/wonderful.png",img)


    writer = imageio.get_writer('animation.gif')
    for i in range(50):
        im = canvas.render()
        writer.append_data(im)
        cam.translate(0.1,0.01,0,0,0)
        points[:,0] = cam.proj_x()
        points[:,1] = cam.proj_y()
        colours = ColorArray(des.colours).rgba
        scatter.set_data(points, edge_color=None, face_color=(0.3, 0.5, 0.8)+ (0.02,), size=des.size)
    writer.close()

#    writer = imageio.save('test.gif', duration=0.05)
#    canvas.events.draw.connect(lambda e: writer.append_data(_screenshot()))
#    canvas.events.close.connect(lambda e: writer.close())
#    timer = app.Timer()
#    timer.connect(update)
#    timer.start(0)
#    vispy.app.run()
    print(str(n) + " points executed in: " + str(round(time.time() - start, 2)) + "secs")


if __name__ == "__main__":

    start = time.time()
    main()

#    #TODO: outputting in b&w?
#    writer = imageio.save('test.mp4', fps=25)
#    for im in imageio.read('test.gif'):
#        writer.append_data(im)
#    writer.close()
