import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from plot_data import PlotData
from translator import Translator

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')


# Import data
data = np.load("des_thinned.npy")

# Clean data, remove nans
data = data[~np.isnan(data).any(axis=1)]

# Truncate, for testing
numpoints = 1000
des = PlotData(data[0:numpoints, 0], data[0:numpoints, 1],
               data[0:numpoints, 2])


ax.scatter(des.x, des.y, des.z, marker="*", c="r", alpha=0.05)
ax.scatter(des.observer.x, des.observer.y, des.observer.z, c="y", marker="o")

translator = Translator(des)

translator.translate(0.5, 0.1, 0, np.pi/2, 0)

ax.scatter(translator.plot_data.x, translator.plot_data.y,
           translator.plot_data.z, marker="*", c='b', alpha=0.05)
ax.scatter(translator.plot_data.observer.x, translator.plot_data.observer.y,
           translator.plot_data.observer.z, marker="o", c="g", s=40)