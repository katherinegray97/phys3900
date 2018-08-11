#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 09:03:01 2018

@author: katiegray
"""
import numpy as np


class Translator(object):
    def __init__(self, plot_data):
        self.plot_data = plot_data

    def translate(self, obs_x, obs_y, obs_z, obs_theta, obs_phi):
        """
        Translates the points as if the observer located at obs_x, obs_y,
        obs_z, looking at obs_theta, obs_phi is at the origin looking down
        the x axis.
        """
        self.plot_data.x = self.plot_data.x - obs_x
        self.plot_data.y = self.plot_data.y - obs_y
        self.plot_data.z = self.plot_data.z - obs_z

        theta = self.plot_data.get_theta() - obs_theta
        phi = self.plot_data.get_phi() - obs_phi
        r = self.plot_data.get_r()

        self.plot_data.x = r*np.cos(theta)*np.sin(phi)
        self.plot_data.y = r*np.sin(theta)*np.sin(phi)
        self.plot_data.z = r*np.cos(phi)

        self.plot_data._set_perspective_data("blue")

        self.plot_data.observer.x = obs_x
        self.plot_data.observer.y = obs_y
        self.plot_data.observer.z = obs_z

        self.plot_data.observer.theta = obs_theta
        self.plot_data.observer.phi = obs_phi