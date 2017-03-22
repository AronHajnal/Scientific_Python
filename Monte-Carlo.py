from __future__ import division
import math
import numpy as np
c = 0
p = 0
i = 1
while abs(math.pi - p) > 0.0001:
    x = np.random.rand()
    y = np.random.rand()
    if x ** 2 + y ** 2 < 1:
        c += 1
    p = (c*4)/i
    i += 1
print p
