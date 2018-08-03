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

class PlotData(object):
    def __init__(self, ra, dec, z):
         """
         The plotting data for each point in a survey

         Params
         ra:  np.ndarray
             right ascension of each point
         dec: np.ndarray
             declination of each point
         z:   np.ndarray
             redshift of each point
         """
         self.length = len(ra)

         # Opacity
         self.alpha = np.zeros((self.length,4))
         self.alpha[:,0] = 1.0

         self.alpha[:,3] = np.random.uniform( 0,1,self.length)

         # Size of points
         self.size = 100

         # Equatorial coord system
         self.ra = ra
         self.dec = dec
         self.z = z


         # Cartersion coord system
         self.x = np.sin(ra)* np.sin(dec) * z
         self.y = np.cos(ra) * np.sin(dec) * z
         self.z = np.cos(dec) * z


    def translate(self, obs_x, obs_y, obs_z, obs_theta, obs_azimuth):
        self.x = self.x + obs_x
        self.y = self.y + obs_y
        self.z = self.z + obs_z


data = np.load("des_thinned.npy")
numpoints = 30
des = PlotData(np.array(data[0:numpoints,0]),np.array(data[0:numpoints,1]),np.array(data[0:numpoints,2]))

ax.scatter(des.x,des.y,des.z, c=des.alpha)
ax.scatter(0,0,0,c="r")

#ax.scatter(0,0.1,1,c="y")
#
#des.translate(0,0.1,1,2,2)




#print ('Executed in:' time.time()-start, 'secs')






