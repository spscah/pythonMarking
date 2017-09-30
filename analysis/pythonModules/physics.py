import numpy as np
import math
import matplotlib.pyplot as plt

class Waves:
    def __init__(self, coordinates, l, phi = 0, multiplier = 1):
        self.phi = phi
        self.multiplier = multiplier
        self.coordinates = coordinates
        self.lam = l
        self.k = (2*math.pi)/l

#y.append(math.sin(wave.multiplier*math.radians(i+wave.phi)))


def makeSquareGrid(size):
    row = [0.0 for i in range(0,size)]
    grid = [row for i in range(0,size)]
    return grid

def calcDistance(pointA,pointB):
    #pass the points in as a tuple
    deltaY = pointA[1] - pointB[1]
    deltaX = pointA[0] - pointB[0]
    return math.sqrt((deltaY**2)+(deltaX**2))




def fillGrid(waveA, waveB, grid):
    #waveA will be at 0,0, waveB will be top right 0,len(row)-1
    for x in range(0,len(grid)):
        for y in range(0,len(grid[x])):
            distanceWaveA = calcDistance(waveA.coordinates,(x,y))
            distanceWaveB = calcDistance(waveB.coordinates,(x,y))
            print(waveB.coordinates,"\t",(x,y))
            print(distanceWaveB)
            
            resultingVal = math.sin(waveA.k+distanceWaveA) + math.sin(waveB.k+distanceWaveB)
            grid[y][x] = resultingVal
    return grid


waveA = Waves((0,0),5)
waveB = Waves((0,0),5)
grid = makeSquareGrid(500)

k = fillGrid(waveA,waveB,grid)

npK = np.array(k)

fig = plt.imshow(npK, interpolation="none")
plt.axis('off')
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()
#make sure that its printing the values correctly
#the above will plot the graph and the 




"""

import numpy as np
import matplotlib.pyplot as plt

H = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])  # added some commas and array creation code

fig = plt.figure(figsize=(6, 3.2))

ax = fig.add_subplot(111)
ax.set_title('colorMap')
plt.imshow(H)
ax.set_aspect('equal')

cax = fig.add_axes([0.12, 0.1, 0.78, 0.8])
cax.get_xaxis().set_visible(False)
cax.get_yaxis().set_visible(False)
cax.patch.set_alpha(0)
cax.set_frame_on(False)
plt.colorbar(orientation='vertical')
plt.show()"""
