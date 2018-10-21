#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pickle
import numpy as np

if __name__ == "__main__":

    # Import data
    full_data = np.load("data/des.npy")

    # Clean data, remove nans and stars
    full_data = full_data[~np.isnan(full_data).any(axis=1)]
    full_data = full_data[full_data[:,8] != 0]

    # Shuffle data to ensure random subset when truncating
    np.random.shuffle(full_data)

    full = open("data/full_data", mode="wb")

    pickle.dump(full_data, full)


    full.close()
