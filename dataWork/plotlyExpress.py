from random import randint
import plotly.express as px

class Die: # Игральный кубик
    def __init__(self, sides = 6):
        self.sides = sides
    
    def roll(self):
        return(randint(1, self.sides))
    

die1 = Die()
die2 = Die(sides=10)

res = []
for roll in range(50000):
    res.append(die1.roll() + die2.roll())

chances = []
maxRes = die1.sides + die2.sides
possibleResults = range(2, maxRes+1)
for r in possibleResults:
    chances.append(res.count(r))

title = "Результат подкидывания шестигранного и десятигранного кубиков 1000 раз"
labels = {'x': 'Result', 'y':'Frequency of Result'}
fig = px.bar(x=possibleResults, y=chances, title=title, labels=labels)

fig.update_layout(xaxis_dtick=1)

fig.show()
