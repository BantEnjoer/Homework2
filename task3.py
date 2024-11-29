from math import *


def find_distance(coords_1, coords_2):
    l1, w1 = coords_1[0], coords_1[1]
    l2, w2 = coords_2[0], coords_2[1]
    l1, w1, l2, w2 = map(radians, [l1, w1, l2, w2])
    a = sin((l2 - l1) / 2) ** 2 + cos(l1) * cos(l2) * sin((w2 - w1) / 2) ** 2
    d = 2 * atan2(sqrt(a), sqrt(1 - a))
    return d * 6371.8

