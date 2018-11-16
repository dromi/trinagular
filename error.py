import math

import numpy as np

def stddev(pixels, coordinates):
    return np.std(np.array(pixels))

def stddev_sum(pixels, coordinates):
    stds = [np.std(p) for p in np.array(pixels).transpose()]
    return sum(stds)

def stddev_avg(pixels, coordinates):
    stds = [np.std(p) for p in np.array(pixels).transpose()]
    return sum(stds) / float(len(stds))

def stddev_avg_times_size(pixels, coordinates):
    return stddev_avg(pixels, coordinates) * area(pixels, coordinates)

def area(pixels, coordinates):
    c1, c2, c3 = coordinates
    dists = [
        (math.hypot(c2[0] - c1[0], c2[1] - c1[1])),
        (math.hypot(c3[0] - c2[0], c3[1] - c2[1])),
        (math.hypot(c3[0] - c1[0], c3[1] - c1[1]))
    ]
    s = (dists[0] + dists[1] + dists[2]) / 2
    area = math.sqrt(s * (s - dists[0]) * (s - dists[1]) * (s - dists[2]))
    return area