import matplotlib.pyplot as plt
from random import choice


class RandonWalk:
    def __init__(self, numPoints=5000):
        self.numPoints = numPoints
        self.x = [0]
        self.y = [0]

    def fillWalk(self):
        while len(self.x) < self.numPoints:
            xDir = choice([1, -1])
            xDist = choice([0, 1, 2, 3, 4])
            xStep = xDist * xDir

            yDir = choice([1, -1])
            yDist = choice([0, 1, 2, 3, 4])
            yStep = yDist * yDir

            if xStep == 0 and yStep == 0: continue

            self.x.append(self.x[-1] + xStep)
            self.y.append(self.y[-1] + yStep)


while True:
    rw = RandonWalk()
    rw.fillWalk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,6))
    num = range(rw.numPoints)
    ax.plot(rw.x, rw.y, linewidth=4, c='blue')
    ax.set_aspect('equal') 
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x[-1], rw.y[-1], c='red', edgecolors='none', s=100)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keepRunning = input("Do you want to see another random walk? (y/n): ")
    if keepRunning == 'n': break
