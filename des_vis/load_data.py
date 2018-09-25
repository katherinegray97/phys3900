#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pickle
import numpy as np


#from itertools import islice
#with open("data/forSam.tab") as myfile:
#    head = list(islice(myfile, 10))
#print (head)


# Import data
#data = np.load("data/full_des.npy")
data = np.load("data/des_thinned.npy")

# Clean data, remove nans
data = data[~np.isnan(data).any(axis=1)]
np.random.shuffle(data)
f = open("data/DESdata", mode="wb")
pickle.dump(data,f)

f.close()


