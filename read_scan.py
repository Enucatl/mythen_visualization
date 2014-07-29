import os
import numpy as np
import matplotlib.pyplot as plt
import glob

import argparse

parser = argparse.ArgumentParser(
    __doc__,
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument(
    "folder",
    nargs=1,
    help="folder where the raw files from the scan are saved"
)

parser.add_argument(
    "--min_pixel",
    nargs='?',
    default=1250,
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
    folder = args.folder[0]
    file_names = glob.glob(os.path.join(folder, "*.raw"))
    #print(file_names)
    datasets = np.vstack([np.loadtxt(file_name, dtype=np.int)[
        args.min_pixel:args.max_pixel, 1]
        for file_name in file_names])
    print(datasets)
    plt.figure()
    plt.imshow(datasets, interpolation="none")
    plt.tight_layout()
    plt.figure()
    integrals = [np.sum(dataset) for dataset in datasets]
    plt.plot(integrals)
    plt.show()
    plt.ion()
    input()
