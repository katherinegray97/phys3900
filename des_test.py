#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 10:42:33 2018

@author: katiegray
"""

import time
import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

start = time.time()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

points = np.load("des_thinned.npy")
# [right ascension, declination, redshift]


numpoints = 100000

dec = np.pi / 2 - points[:,1]
xs = np.sin(points[:,0]) * np.sin(dec) * points[:,2]
ys = np.cos(points[:,0]) * np.sin(dec) * points[:,2]
zs = np.cos(dec)*points[:,2]
 
ax.scatter(xs[0:numpoints],ys[0:numpoints],zs[0:numpoints],c='b')

print 'Executed in:', time.time()-start, 'secs' 


 

