#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 09:03:19 2018

@author: katiegray
"""
import numpy as np


class Survey(object):
    def __init__(self, ras, decs, zs, threshold = sys.maxsize):
        """
        The plotting data for points in a survey. Points are stored taken in
        equatorial coords but stored as Cartesian coordinates.

        Params
        ras:  np.ndarray
            right ascension of each point
        decs: np.ndarray
            decslination of each point
        zs:   np.ndarray
            redshift of each point
        """

        # Cartersion coord system
        decs = np.pi / 2 - decs
        self._full_xs = np.sin(ras) * np.sin(decs) * zs
        self._full_ys = np.cos(ras) * np.sin(decs) * zs
        self._full_zs = np.cos(decs) * zs

        self.set_threshold(threshold)

    def set_threshold(self, threshold):
        self._threshold = threshold
        self.xs = self._full_xs[self.get_r() < self.threshold]
        self.ys = self._full_ys[self.get_r() < self.threshold]
        self.zs = self._full_zs[self.get_r() < self.threshold]

        # Number of points below the threshold
        self.legnth = len(self.xs)

        # Plotting sizes of points
        self.size = 20*(1 - self.xs/self.threshold)

        # Random colours
        self.alpha = np.zeros((self.length, 4))
        self.alpha[:,0] = np.random.rand(self.length)
        self.alpha[:,1] = np.random.rand(self.length)
        self.alpha[:,2] = np.random.rand(self.length)
        self.alpha[:, 3] = 1-abs(self.xs/np.amax(self.xs))


    def get_theta(self):
        """
        Returns theta [rads] of each point expressed in spherical coords.
        (Note, theta is the azimuthal angle in the x-y plane, 0 < theta < 2pi)
        """

        return np.where((self.ys) == 0, 0, np.arctan2(self.ys, self.xs))

    def get_phi(self):
        """
        Returns phi [rads] of each point expressed in spherical coords.
        (Note, phi is the polar angle from the z axis, 0 < phi < pi)
        """

        return np.where((self.zs) == 0, 0, np.arccos((self._zs)/self.get_r()))

    def get_r(self):
        """
        Returns r [m] of each point expressed in spherical coods.
        (Note, r is the distance from the origin)
        """
        return np.sqrt(np.power(self.xs, 2) + np.power(self.ys, 2) +
                       np.power(self.zs, 2))


    def print(self):
        print(np.dstack([self.xs[0:3], self.ys[0:3], self.zs[0:3]]))


