#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pickle
import numpy as np


#from itertools import islice
#with open("data/forSam.tab") as myfile:
#    head = list(islice(myfile, 10))
#print (head)


# Import data
full_data = np.load("data/full_des.npy")
thin_data = np.load("data/des_thinned.npy")

# Clean data, remove nans
full_data = full_data[~np.isnan(full_data).any(axis=1)]
np.random.shuffle(full_data)
thin_data = thin_data[~np.isnan(thin_data).any(axis=1)]
np.random.shuffle(thin_data)


full = open("data/full_data", mode="wb")
thin = open("data/thin_data", mode="wb")

pickle.dump(full_data,full)
pickle.dump(thin_data,thin)

full.close()
thin.close()


