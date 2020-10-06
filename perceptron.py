import numpy as np

list1 = [
[1, 6],
[3, 3],
[-3, 2],
[3, -5],
[-4, -2],
[0, 5]
]
d = [-1, -1, 1, -1, 1, 1]


def signum(x):
    if x ==0:
        return 0
    if x < 0:
        return -1
    if x > 0:
        return 1
def product(l1, l2):
    return l1[0]*l2[0] + l1[1]*l2[1]

def funn():
    w = [0, 0]
    for each_iteration in range(10):
        for i in range(len(list1)):
            t = signum(product(w, list1[i]))
            if t != d[i]:
                fac = signum(product(w, list1[i]))
                w += (d[i] - fac)*list1[i]

funn()
