#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pickle
import numpy as np

if __name__ == "__main__":

    # Import data
    # Data format should be a numpy object with the following columns:
    # (Note that the format - units etc. - should exactly correspond to that of the columns in the Dark Energy Survey Y3 gold catalogue.)
    # RA | DEC | MU_MEAN_MODEL_G | MU_MEAN_MODEL_R | MU_MEAN_MODEL_I | MU_MEAN_MODEL_Z | DNF_ZMC_MOF | DNF_ZMC_SOF | EXTENDED_CLASS_COADD
    full_data = np.load("data/des.npy")

    # Clean data, remove nans and stars
    full_data = full_data[~np.isnan(full_data).any(axis=1)]
    full_data = full_data[full_data[:,8] != 0]
    full_data = full_data[full_data[:,8] != 1]

    # Shuffle data to ensure random subset when truncating
    np.random.shuffle(full_data)

    full = open("data/full_data", mode="wb")

    pickle.dump(full_data, full)


    full.close()
