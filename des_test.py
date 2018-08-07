"""
Created on Thu Jul 12 10:42:33 2018

@author: katiegray
"""


import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

class PlotData(object):
    def __init__(self, ra, dec, z):
         """
         The plotting data for point in a survey. Points are stored as
         Cartesian coordinates. Observer is initially at origin, looking down
         x axis.

         Params
         ra:  np.ndarray
             right ascension of each point
         dec: np.ndarray
             declination of each point
         z:   np.ndarray
             redshift of each point
         """
         # Equatorial coord system - private variables, not to be modified
         self._ra = ra
         self._dec = dec
         self._z = z

         # Cartersion coord system
         dec = np.pi / 2 - dec
         self.x = np.sin(ra)* np.sin(dec) * z
         self.y = np.cos(ra) * np.sin(dec) * z
         self.z = np.cos(dec) * z

         self.obs_x = 0
         self.obs_y = 0
         self.obs_z = 0
         self.obs_theta = 0
         self.obs_phi = np.pi/2

         # Number of data points
         self.length = len(ra)
         # Setting threshold - currently arbitrary
         self.threshold = max(self.get_r())*0.8

         self._set_perspective_data("red")


    def _set_perspective_data(self, colour):
        self.close_x = self.x[self.get_r() < self.threshold]
        self.close_y = self.y[self.get_r() < self.threshold]
        self.close_z = self.z[self.get_r() < self.threshold]

        self.num_threshold = len(self.close_x)

        # Plotting size of points
        self.size =  20*(1 - self.get_close_r()/self.threshold)

        # Alpha value of points
        self.alpha = np.zeros((self.num_threshold,4))
        if (colour == "red"):
            self.alpha[:,0] = 1.0
        else:
            self.alpha[:,1] = 1.0

        self.alpha[:,3] = 1-(self.get_close_r()*(1.0/self.threshold))

    def translate(self, obs_x, obs_y, obs_z, obs_theta, obs_phi):
        """
        Translates the points as if the observer located at obs_x,obs_y,obs_z,
        looking at obs_theta, obs_phi is at the origin looking down the x axis.
        """

        self.x = self.x - obs_x
        self.y = self.y - obs_y
        self.z = self.z - obs_z


        theta = self.get_theta() - obs_theta
        phi = self.get_phi() - obs_phi
        r = self.get_r()


        self.x = r*np.cos(theta)*np.sin(phi)
        self.y = r*np.sin(theta)*np.sin(phi)
        self.z = r*np.cos(phi)

        self._set_perspective_data("blue")

        self.obs_x = obs_x
        self.obs_y = obs_y
        self.obs_z = obs_z

        self.obs_theta = obs_theta
        self.obs_phi = obs_phi

    def get_theta(self):
        """
        Returns theta [rad] of each point expressed in spherical coords.
        (Note, theta is the azimuthal angle in the x-y plane, 0 < theta < 2pi)
        """

        return np.where((self.y-self.obs_y) == 0, 0, np.arctan2(self.y-self.obs_y,self.x-self.obs_x))

    def get_phi(self):
        """
        Returns phi [rad] of each point expressed in spherical coords.
        (Note, phi is the polar angle from the z axis, 0 < phi < pi)
        """

        return np.where((self.z-self.obs_z) == 0, 0, np.arccos((self.z-self.obs_z)/self.get_r()))


    def get_r(self):
        """
        Returns r [m] of each point expressed in spherical coods.
        (Note, r is the distance from the origin)
        """

        return  np.sqrt(np.power(self.x-self.obs_x,2) + np.power(self.y-self.obs_y,2) + np.power(self.z-self.obs_z,2))


    def get_close_r(self):
        """
        Returns the radius of the points closer than the threshold
        """

        return self.get_r()[self.get_r() < self.threshold]

    def print(self):
        print(np.dstack([self.x[0:3], self.y[0:3], self.z[0:3]]))

# Import data
data = np.load("des_thinned.npy")

# Clean data, remove nans
data = data[~np.isnan(data).any(axis=1)]

# Truncate, for testing
numpoints = 1000
des = PlotData(data[0:numpoints,0],data[0:numpoints,1],data[0:numpoints,2])


ax.scatter(des.x,des.y,des.z, marker = "*", c= "r", alpha = 0.05)
ax.scatter(des.obs_x, des.obs_y, des.obs_z, c="y", marker = "o")


des.translate(0.5, 0.1, 0,np.pi/2, 0)

ax.scatter(des.x, des.y, des.z,marker = "*",c = 'b' ,alpha = 0.05 )
ax.scatter(des.obs_x, des.obs_y, des.obs_z, marker = "o", c = "g", s = 40)





