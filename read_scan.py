import os
import numpy as np
import matplotlib.pyplot as plt
import glob
import h5py

import argparse

parser = argparse.ArgumentParser(
    __doc__,
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument(
    "file",
    nargs=1,
    help="hdf5 file"
)

parser.add_argument(
    "--min_pixel",
    nargs='?',
    default=0,
    type=int,
    help="first pixel"
)

parser.add_argument(
    "--max_pixel",
    nargs='?',
    default=2560,
    type=int,
    help="last pixel"
)

if __name__ == '__main__':
    args = parser.parse_args()
    file_name = args.file[0]
    input_file = h5py.File(file_name, "r")
    datasets = np.vstack(
        [dataset[args.min_pixel:args.max_pixel]
         for dataset in input_file["raw_images"].values()])
    input_file.close()
    print(datasets, np.max(datasets))
    plt.figure()
    plt.imshow(datasets, interpolation="none", aspect='auto')
    plt.tight_layout()
    plt.figure()
    integrals = [np.sum(dataset) for dataset in datasets]
    plt.plot(integrals)
    plt.show()
    plt.ion()
    input()
