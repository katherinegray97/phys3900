# PHYS3900 Capstone Project
## DES Flythough 

This aim of this project is to create a fly-through visualisation of the [Dark Energy Survey](https://www.darkenergysurvey.org/the-des-project/overview/). 

Note that this repository does not contain data. Data should be loaded into a pickle data stream using load_data.py. 

plot.py can then be used to create fly-through simulation. plot.py takes command line arguments of: 
1. an appropriate choice of plotting library - 'vispy' or 'matplotlib' (ffmpeg support is required for matplotlib)
2. An integer to divde the dataset by for quick plotting of a random subset of data
3. An integer number of frames to plot

The flight path can be altered in the vispy_plot or matplotlib_plot methods in plot.py. It is currently set to a linear flight path.
