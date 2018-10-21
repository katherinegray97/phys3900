# PHYS3900 Capstone Project
## DES Flythough 

This aim of this project is to create a fly-through visualisation of the [Dark Energy Survey](https://www.darkenergysurvey.org/the-des-project/overview/). 


## Dependencies
* This repository does not contain data. Data must be provided as a numpy object saved in data/des.npy. The columns required for the visualisation (which exactly correspond to the columns in the Y3 Gold catalogue of the Dark Energy Survey -inc. units, formatting etc.) are: 
RA | DEC | MU_MEAN_MODEL_G | MU_MEAN_MODEL_R | MU_MEAN_MODEL_I | MU_MEAN_MODEL_Z | DNF_ZMC_MOF | DNF_ZMC_SOF | EXTENDED_CLASS_COADD

* Required Python modules/libraries: 
  - [vispy](http://vispy.org/)
  - [imageio](https://pypi.org/project/imageio/)
  - [matplotlib](https://matplotlib.org/index.html)
  - [numpy](http://www.numpy.org/)
  - [pickle](https://docs.python.org/2/library/pickle.html)
  - [sys](https://docs.python.org/3/library/sys.html)
  - [os](https://docs.python.org/3/library/os.html)
  - [time](https://docs.python.org/3/library/time.html)

* Required external software: 
    - [ffmpeg](https://www.ffmpeg.org/)

## Usage
Data should be first be loaded into a pickle data stream using load_data.py. 

plot.py can then be used to create fly-through simulation. plot.py takes command line arguments of: 
1. an appropriate choice of plotting library - 'vispy' or 'matplotlib' (ffmpeg support is required for matplotlib)
2. An integer to divde the dataset by for quick plotting of a random subset of data
3. An integer number of frames to plot
3. An integer number of frames per second

The flight path can be altered in the vispy_plot or matplotlib_plot methods in plot.py. It is currently set to a linear flight path flying out from Earth. 
