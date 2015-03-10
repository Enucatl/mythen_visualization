import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

import argparse

parser = argparse.ArgumentParser(
    __doc__,
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument(
    "file",
    nargs=1,
    help="file"
)

if __name__ == '__main__':
    args = parser.parse_args()
    file_name = args.file[0]
    image = np.fromfile(file_name, dtype=np.int32).reshape((619, 487))
    print(image)
    plt.figure()
    im_show = plt.imshow(image, interpolation="none", aspect='auto')
    limits = stats.mstats.mquantiles(image, prob=[0.02, 0.98])
    im_show.set_clim(*limits)
    print(limits)
    print(np.sum(image[image >=0]))
    plt.tight_layout()
    #plt.figure()
    #integrals = [np.sum(dataset) for dataset in datasets]
    #plt.plot(integrals)
    plt.show()
    plt.ion()
    input()
