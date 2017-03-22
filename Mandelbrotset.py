import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
z = 0 + 0*1j #initial value: z0
xt = np.linspace(-2,0.5,250)
yt = np.linspace(-1,1,200)
constants =  [x+y*1j for x in xt for y in yt] #set up the grid of c-s in the complex plane
results = []
for c in constants:
    for n in range(100):
        z = z ** 2 + c #apply the function a 100 times for each c
    if math.isnan(z.real): #checking the real part is enough
        results.append(0) #we put a result of zero if the value diverges
    else:
        results.append(c) #we save c
    z = 0 #important to set back z after we finished with a c
img = np.zeros((250,200)) #initialise grid for picture with all zeros
for a in range(len(xt)):
    for b in range(len(yt)):
        if xt[a]+yt[b]*1j in results: #for every number in the grid we check if it diverged
            img[a][b] = 1 #if it didnt we set its coordinate to 1
imgplot = plt.imshow(img)
plt.xlabel('Re(c)')
plt.ylabel('Im(c)')
plt.title('The Mandelbrot set')
plt.show()
