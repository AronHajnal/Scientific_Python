from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

def galton(n, k):
    x = 1
    s = 0
    ii = []
    xx = []
    for i in range(1,n):
        for j in range(x):
            desc = np.random.poisson(k)
            s += desc
        x = s
        ii.append(i)
        xx.append(x)
    plt.plot(ii,xx)
    plt.show()
