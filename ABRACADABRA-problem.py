import numpy as np

w = ""
a = "abracadabra"
s = True
counter = 0

while(s):
    counter = counter+1
    i = np.random.randint(97,123)
    c = chr(i)
    w = w + c
    if len(w) > len(a):
        w = w[1:len(w)]
    if w == a:
        s = False
        print "Got it!"
        print counter
