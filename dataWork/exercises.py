import matplotlib.pyplot as plt
from random import choice
from random import randint
import plotly.express as px

# 15. Генерирование данных

# 15.1, 15.3
# xValues = range(0, 5001)
# yValues = [x**3 for x in xValues]

# fig, ax = plt.subplots()
# plt.scatter(xValues, yValues, s = 10, c=xValues, cmap = plt.cm.Blues)

# plt.show()

# 15.3, 15.4, 15.5
class RandomWalk:
    def __init__(self, numPoints=5000):
        self.numPoints = numPoints
        self.x = [0]
        self.y = [0]

    def fillWalk(self):
        while len(self.x) < self.numPoints:
            xStep = self.getStep()
            yStep = self.getStep()

            if xStep == 0 and yStep == 0: continue

            self.x.append(self.x[-1] + xStep)
            self.y.append(self.y[-1] + yStep)

    def getStep(self):
        dir = choice([1, -1])
        dist = choice([0, 1, 2, 3, 4])
        return dir * dist


# while True:
#     rw = RandomWalk()
#     rw.fillWalk()

#     plt.style.use('classic')
#     fig, ax = plt.subplots(figsize=(15,6))
#     num = range(rw.numPoints)
#     ax.plot(rw.x, rw.y, linewidth=4, c='blue')
#     ax.set_aspect('equal') 
#     ax.scatter(0, 0, c='green', edgecolors='none', s=100)
#     ax.scatter(rw.x[-1], rw.y[-1], c='red', edgecolors='none', s=100)

#     ax.get_xaxis().set_visible(False)
#     ax.get_yaxis().set_visible(False)
#     plt.show()

#     keepRunning = input("Do you want to see another random walk? (y/n): ")
#     if keepRunning == 'n': break

# 15.6
class Die: # Игральный кубик
    def __init__(self, sides = 6):
        self.sides = sides
    
    def roll(self):
        return(randint(1, self.sides))
    

# die1 = Die(sides=8)
# die2 = Die(sides=8)

# res = []
# for roll in range(1000):
#     res.append(die1.roll() + die2.roll())

# chances = []
# maxRes = die1.sides + die2.sides
# possibleResults = range(2, maxRes+1)
# for r in possibleResults:
#     chances.append(res.count(r))

# title = "Результат подкидывания двух восьмигранных кубиков 1000 раз"
# labels = {'x': 'Result', 'y':'Frequency of Result'}
# fig = px.bar(x=possibleResults, y=chances, title=title, labels=labels)

# fig.update_layout(xaxis_dtick=1)

# fig.show()

#15.7
# die1 = Die()
# die2 = Die()
# die3 = Die()
# res = []
# for i in range(1001):
#     res.append(die1.roll() + die2.roll() + die3.roll())

# possibleResults = range(3, die1.sides + die2.sides + die3.sides+1)
# chances = []
# for ps in possibleResults:
#     chances.append(res.count(ps))

# fig = px.bar(x=possibleResults, y=chances)
# fig.show()

# 15.8 
# die1 = Die(sides=8)
# die2 = Die(sides=8)

# res = []
# for roll in range(1000):
#     res.append(die1.roll() * die2.roll())

# chances = []
# maxRes = die1.sides * die2.sides
# possibleResults = range(2, maxRes+1)
# for r in possibleResults:
#     chances.append(res.count(r))

# title = "Результат подкидывания двух восьмигранных кубиков 1000 раз"
# labels = {'x': 'Result', 'y':'Frequency of Result'}
# fig = px.bar(x=possibleResults, y=chances, title=title, labels=labels)

# fig.update_layout(xaxis_dtick=1)

# fig.show()

# 15.10
# rw = RandomWalk()
# rw.fillWalk()
# fig = px.line(rw.x, rw.y)
# fig.show()

die1 = Die()
die2 = Die(8)

res = []
for i in range(1001): res.append(die1.roll() + die2.roll())
possRes = range(2, die1.sides + die2.sides + 1)
chances = []
for p in possRes:
    chances.append(res.count(p))

fig, ax = plt.subplots()
ax.bar(possRes, chances, width=1, edgecolor='white')

plt.show()