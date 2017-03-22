from __future__ import division
import random
import numpy as np
import matplotlib.pyplot as plt

def Polya(b,w):

    pp = []
    pp.append(0)

    for i in range(1000):

        r  = random.random()

        p = b/(b+w)
    
        if(p>r):
            b += 1
        else:
            w += 1
    
        pp.append(p)
        d = pp[i]-pp[i-1]
        if(abs(d)<0.001):
            return p
            
hist = []
for i in range(10000):
    hist.append(Polya(2,3))
    
bins = np.arange(0, 1, 0.01)
plt.hist(hist, bins)
plt.show()
