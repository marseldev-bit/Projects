from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('C:\\Users\\marse\\OneDrive\\Рабочий стол\\Projects\\dataWork\\weatherData\\death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
headerRow = next(reader)

dates, highs, lows = [], [], []
for row in reader:
    currentDate = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        highs.append(int(row[3]))
        lows.append(int(row[4]))
    except: 
        print(f"Missing data for {currentDate}")
    else: dates.append(currentDate)

fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

ax.set_title("Daily high and low temperatures, 2021\nDeath Valley, CA", fontsize=16)
ax.set_ylabel("Temperature (F)")
fig.autofmt_xdate()

plt.show()