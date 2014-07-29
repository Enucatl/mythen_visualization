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

if __name__ == '__main__':
    args = parser.parse_args()
    folder = args.folder
    file_names = glob.glob(os.path.join(folder, "*.raw"))
    print(file_names)
    #datasets = np.
