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
         self.alpha = np.ones(self.length)
         # Size of points 
         self.size = np.ones(self.length)
        
         # Equatorial coord system
         self.ra = ra
         self.dec = dec
         self.z = z
        
        
         # Cartersion coord system 
         self.x = np.sin(ra)* np.sin(dec) * z 
         self.y = np.cos(ra) * np.sin(dec) * z
         self.z = np.cos(dec) * z
           
    
    def translate(self, obs_x, obs_y, obs_z, obs_theta, obs_azimuth):
        self.x = self.x + 1000
            
        
data = np.load("des_thinned.npy")
numpoints = 100
des = PlotData(np.array(data[0:numpoints,0]),np.array(data[0:numpoints,1]),np.array(data[0:numpoints,2]))

ax.scatter(des.x,des.y,des.z,c='b')

translate(1,2,2,2,2)

ax.scatter(des.x,des.y,des.z,c='g')

#print ('Executed in:' time.time()-start, 'secs')




 

