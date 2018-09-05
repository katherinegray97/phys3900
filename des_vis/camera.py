#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 07:12:22 2018

@author: katiegray
"""

import numpy as np


class Camera(object):
    def __init__(self, survey, v_x = 1920, v_y = 1080, fov = 70):
        self.x = 0
        self.y = 0
        self.z = 0
        self.theta = np.pi
        self.phi = 0
        self.survey = survey

        self.v_x = v_x
        self.v_y = v_y
        self.aspect = v_x/v_y
        self.fov = fov
        self.fov_w = 0.5 * fov * np.pi / 180
        self.fov_h = self.fov_w / self.aspect


    def get_points_x(self):
        return np.arctan2(self.survey.ys, self.survey.xs) / np.tan(self.fov_w)

    def get_points_y(self):
        return np.arctan2(self.survey.zs, self.survey.ys) / np.tan(self.fov_h)

    def _get_theta(self):
        """
        Returns theta [rads] of each point expressed in spherical coords.
        (Note, theta is the azimuthal angle in the x-y plane, 0 < theta < 2pi)
        """

        return np.where((self.y) == 0, 0, np.arctan2(self.y, self.x))

    def _get_phi(self):
        """
        Returns phi [rads] of each point expressed in spherical coords.
        (Note, phi is the polar angle from the z axis, 0 < phi < pi)
        """
        if(self._get_r()!= 0):
            if(self.z/self._get_r() > 1):
                print("problem")

        return np.where((self._get_r()) == 0, 0, np.arccos(self.z/self._get_r()))

    def _get_r(self):
        """
        Returns r [m] of each point expressed in spherical coods.
        (Note, r is the distance from the origin)
        """

        return np.sqrt(np.power(self.x, 2) + np.power(self.y, 2) +
                       np.power(self.z, 2))

    def translate(self, x, y, z, theta, phi):
        """
        Translates the camera's survey as if the camera was moving x, y, z
        units in each respective direction and rotating theta radians
        anticlockwise about the z axis (if looking towards negative z) and phi
        radians anticlockwise about the y axis (if looking towards negative y).
        """
        self.survey.translate(-x, -y, -z, -theta, -phi)

        self.x += x
        self.y += y
        self.z += z

        # Get new radii
#        r = self._get_r()
#
#        # Rotate
#        theta = self._get_theta() + theta
#        phi = self._get_phi() + phi
#
#        # Set rotation
#        self.x = r*np.cos(theta)*np.sin(phi)
#        self.y = r*np.sin(theta)*np.sin(phi)
#        self.z = r*np.cos(phi)

