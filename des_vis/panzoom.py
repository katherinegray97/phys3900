#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 11:00:42 2018

@author: katiegray
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 10:16:43 2018

@author: katiegray
"""

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



data = np.zeros((50, 3))
data[:,0] = np.linspace(0,1,num = 50)
data[:,1] = data[:,0]
data[:,2] = 0


des = Survey(data[:, 0], data[:, 1], data[:, 2], threshold = 0.9, xs = data[:, 0], ys = data[:, 1], true_zs = data[:, 2])
cam = Camera(des)
points =np.zeros((50, 3))
canvas = vispy.scene.SceneCanvas(bgcolor='w')
view = canvas.central_widget.add_view()

scatter = visuals.Markers()
scatter.set_data(points)
view.add(scatter)
view.camera = 'panzoom'
view.camera.center = (0,0,0)
view.camera.fov = 70
view.camera.set_range(x=(0,1), y =(0,1))

print("state", view.camera.get_state())

axis = visuals.XYZAxis(parent=view.scene)

writer = imageio.get_writer('vispy_out/vispy_animation.gif')
max_i = 4
points = data
points[:,0] = cam.proj_x()
points[:,1] = cam.proj_y()
for i in range(max_i):
    print(i)
    points = points + 0.001
    scatter.set_data(points)

    im = canvas.render()
    writer.append_data(im)
writer.close()



