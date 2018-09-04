#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 09:03:19 2018

@author: katiegray
"""
import numpy as np
import sys

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
        """
        Returns theta [rads] of each point expressed in spherical coords.
        (Note, theta is the azimuthal angle in the x-y plane, 0 < theta < 2pi)
        """
        self._threshold = threshold
        self.xs = self._full_xs[self._get_r() < threshold]
        self.ys = self._full_ys[self._get_r() < threshold]
        self.zs = self._full_zs[self._get_r() < threshold]

        # Number of points below the threshold
        self.length = len(self.xs)

        # Plotting sizes of points
        self.size = 20*(1 - self.xs/threshold)

        # Random colours
        self.alpha = np.zeros((self.length, 4))
        self.alpha[:,0] = np.random.rand(self.length)
        self.alpha[:,1] = np.random.rand(self.length)
        self.alpha[:,2] = np.random.rand(self.length)
        self.alpha[:, 3] = 1-abs(self.xs/np.amax(self.xs))


    def _get_theta(self):
        """
        Returns theta [rads] of each point expressed in spherical coords.
        (Note, theta is the azimuthal angle in the x-y plane, 0 < theta < 2pi)
        """

        return np.where((self._full_ys) == 0, 0, np.arctan2(self._full_ys, self._full_xs))

    def _get_phi(self):
        """
        Returns phi [rads] of each point expressed in spherical coords.
        (Note, phi is the polar angle from the z axis, 0 < phi < pi)
        """

        return np.where((self._full_zs) == 0, 0, np.arccos((self._full_zs)/self._get_r()))

    def _get_r(self):
        """
        Returns r [m] of each point expressed in spherical coods.
        (Note, r is the distance from the origin)
        """

        return np.sqrt(np.power(self._full_xs, 2) + np.power(self._full_ys, 2) +
                       np.power(self._full_zs, 2))

    def translate(self, x, y, z, theta, phi):
        """
        Translates the points x, y, z units in each respective direction and
        rotates the points theta radians anticlockwise about the z axis (if
        looking towards negative z) and phi radians anticlockwise about the y
        axis (if looking towards negative y).
        """

        # Translate
        self._full_xs += x
        self._full_ys += y
        self._full_zs += z

        # Get new radii
        r = self._get_r()

        # Rotate
        theta = self._get_theta() + theta
        phi = self._get_phi() + phi

        # Set rotation
        self._full_xs = r*np.cos(theta)*np.sin(phi)
        self._full_ys = r*np.sin(theta)*np.sin(phi)
        self._full_zs = r*np.cos(phi)

        # Update thresholds
        self.set_threshold(self._threshold)

    def print(self):
        print(np.dstack([self.xs[0:3], self.ys[0:3], self.zs[0:3]]))


