import math


def euclidean_Distance(l1, l2):
    dist = 0.0
    for i in range(len(l1)-1):
        dist += (l1[i]-l2[i])**2
    return round(math.sqrt(dist), 3)
