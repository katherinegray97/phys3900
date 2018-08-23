#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 09:03:19 2018

@author: katiegray
"""
import numpy as np


class PlotData(object):
    def __init__(self, ra, dec, z):
        """
        The plotting data for point in a survey. Points are stored as
        Cartesian coordinates. Observer is initially at origin, looking down
        x axis.

        Params
        ra:  np.ndarray
        right ascension of each point
        dec: np.ndarraydeclination of each point
        z:   np.ndarray
        redshift of each point
        """

        # Equatorial coord system - private variables, not to be modified
        self._ra = ra
        self._dec = dec
        self._z = z

        # Observer
        self.observer = Observer(0, 0, 0, np.pi,0)

        # Cartersion coord system
        dec = np.pi / 2 - dec
        self.x = np.sin(ra) * np.sin(dec) * z
        self.y = np.cos(ra) * np.sin(dec) * z
        self.z = np.cos(dec) * z

        # Number of data points
        self.length = len(ra)

        self.threshold = 0.9

        self.alpha = np.zeros((self.length, 4))
        self.alpha[:,0] = np.random.rand(self.length)
        self.alpha[:,1] = np.random.rand(self.length)
        self.alpha[:,2] = np.random.rand(self.length)

        self._set_perspective_data()

    def _set_perspective_data(self):
        self.close_x = self.x[self.get_r() < self.threshold]
        self.close_y = self.y[self.get_r() < self.threshold]
        self.close_z = self.z[self.get_r() < self.threshold]
        self.close_alpha = self.alpha[self.get_r()< self.threshold]

        self.num_threshold = len(self.close_x)

        # Plotting size of points
        self.close_size = 20*(1 - self.get_close_r()/self.threshold)

        self.close_alpha[:, 3] = 1-(self.get_close_r()*(1.0/self.threshold))

    def get_theta(self):
        """
        Returns theta [rad] of each point expressed in spherical coords.
        (Note, theta is the azimuthal angle in the x-y plane, 0 < theta < 2pi)
        """

        return np.where((self.y) == 0, 0,
                        np.arctan2(self.y,
                                   self.x))

    def get_phi(self):
        """
        Returns phi [rad] of each point expressed in spherical coords.
        (Note, phi is the polar angle from the z axis, 0 < phi < pi)
        """

        return np.where((self.z) == 0,
                        0, np.arccos((self.z)/self.get_r()))

    def get_r(self):
        """
        Returns r [m] of each point expressed in spherical coods.
        (Note, r is the distance from the origin)
        """
        return np.sqrt(np.power(self.x, 2) +
                       np.power(self.y, 2) +
                       np.power(self.z, 2))

    def get_obs_r(self):
        """
        Returns r [m] of each point expressed in spherical coods.
        (Note, r is the distance from the origin)
        """
        return np.sqrt(np.power(self.x-self.observer.x, 2) +
                       np.power(self.y-self.observer.y, 2) +
                       np.power(self.z-self.observer.z, 2))

    def get_close_r(self):
        """
        Returns the radius of the points closer than the threshold
        """

        return self.get_r()[self.get_r() < self.threshold]

    def print(self):
        print(np.dstack([self.x[0:3], self.y[0:3], self.z[0:3]]))


class Observer(object):
    def __init__(self, x, y, z, theta, phi):
        self.x = x
        self.y = y
        self.z = z
        self.theta = theta%(2*np.pi)
        self.phi = phi
