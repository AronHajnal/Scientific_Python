import random
import matplotlib.pyplot as plt
i = 0
t = 0
money = True
w = 10
tt = []
ww = []

while(money and i < 1000):
    i += 1
    b = 1
    x = 0
    
    while(x<=0 and money):
        t +=1
        if random.random() > 0.5:
            x = 1
        else:
            x = -1
        b *= 2
        w += b*x
        tt.append(t)
        ww.append(w)
        if w<0:
            money = False

plt.plot(tt,ww)
