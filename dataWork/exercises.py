import matplotlib.pyplot as plt
import csv
from pathlib import Path
from datetime import datetime
import json
import plotly.express as px

# 16. Загрузка данных

#16.1
# pathSitka = Path('C:\\Users\\marse\\OneDrive\\Рабочий стол\\Projects\\dataWork\\weatherData\\sitka_weather_2021_full.csv')
# pathDeathValley = Path('C:\\Users\\marse\OneDrive\\Рабочий стол\\Projects\\dataWork\\weatherData\\death_valley_2021_full.csv')

# lines = pathSitka.read_text().splitlines()
# sitkaReader = csv.reader(lines)
# lines = pathDeathValley.read_text().splitlines()
# DVReader = csv.reader(lines)

# next(sitkaReader)
# next(DVReader)

# print(DVReader)

# sitkaPRCP, DVPRCP, dates = [], [], []

# for s in sitkaReader: 
#     sitkaPRCP.append(float(s[5]))
#     dates.append(datetime.strptime(s[2], '%Y-%m-%d'))
# for dv in DVReader: DVPRCP.append(float(dv[3]))

# fig, ax = plt.subplots()
# ax.plot(dates, sitkaPRCP, color='purple')
# ax.plot(dates, DVPRCP, color='orange')
# ax.fill_between(dates, sitkaPRCP, DVPRCP, color="purple", alpha=0.3)

# ax.set_title("Уровень осадком в Ситке и Долине смерти (Калифорния)\n2021", fontsize=16)
# plt.show()

# 16.2
# path = Path('C:\\Users\\marse\\OneDrive\\Рабочий стол\\Projects\\dataWork\\weatherData\\death_valley_2021_simple.csv')
# lines = path.read_text().splitlines()

# reader = csv.reader(lines)
# headerRow = next(reader)

# dates, highs, lows = [], [], []
# for row in reader:
#     currentDate = datetime.strptime(row[2], '%Y-%m-%d')
#     try:
#         highs.append(int(row[3]))
#         lows.append(int(row[4]))
#     except: 
#         print(f"Missing data for {currentDate}")
#     else: dates.append(currentDate)

# fig, ax = plt.subplots()
# ax.plot(dates, highs, color='red', alpha=0.5)
# ax.plot(dates, lows, color='blue', alpha=0.5)
# ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# plt.ylim(20, 160)

# ax.set_title("Daily high and low temperatures, 2021\nDeath Valley, CA", fontsize=16)
# ax.set_ylabel("Temperature (F)")
# fig.autofmt_xdate()

# plt.show()

# 16.4
# pathSitka = Path('C:\\Users\\marse\\OneDrive\\Рабочий стол\\Projects\\dataWork\\weatherData\\sitka_weather_2021_full.csv')
# pathDeathValley = Path('C:\\Users\\marse\OneDrive\\Рабочий стол\\Projects\\dataWork\\weatherData\\death_valley_2021_full.csv')

# lines = pathSitka.read_text().splitlines()
# sitkaReader = csv.reader(lines)
# lines = pathDeathValley.read_text().splitlines()
# DVReader = csv.reader(lines)

# sitkaHead = next(sitkaReader)
# DVHead = next(DVReader)

# sitkaIndex, DVIndex = 0, 0
# for index, name in enumerate(sitkaHead): 
#     if name == 'PRCP':
#         sitkaIndex = index
#         break 
# for index, name in enumerate(DVHead): 
#     if name == 'PRCP':
#         DVIndex = index
#         break 

# print(DVReader)

# sitkaPRCP, DVPRCP, dates = [], [], []

# for s in sitkaReader: 
#     sitkaPRCP.append(float(s[sitkaIndex]))
#     dates.append(datetime.strptime(s[2], '%Y-%m-%d'))
# for dv in DVReader: DVPRCP.append(float(dv[DVIndex]))

# fig, ax = plt.subplots()
# ax.plot(dates, sitkaPRCP, color='purple')
# ax.plot(dates, DVPRCP, color='orange')
# ax.fill_between(dates, sitkaPRCP, DVPRCP, color="purple", alpha=0.3)

# ax.set_title("Уровень осадком в Ситке и Долине смерти (Калифорния)\n2021", fontsize=16)
# plt.show()

# 16.6 Выполнен в файле geoJson.py

# 16.7
# path = Path('C:\\Users\\marse\\OneDrive\\Рабочий стол\\Projects\\dataWork\\eqData\\eq_data_1_day_m1.geojson')
# eqData = json.loads(path.read_text())

# path = Path('C:\\Users\\marse\\OneDrive\\Рабочий стол\\Projects\\dataWork\\eqData\\readable_eq_data.geojson')
# path.write_text(json.dumps(eqData, indent=4))

# eqDicts = eqData['features']

# mags, lons, lats, eqTitles = [], [], [], []
# for key in eqDicts:
#     mags.append(key['properties']['mag'])
#     lons.append(key['geometry']['coordinates'][0])
#     lats.append(key['geometry']['coordinates'][1])
#     eqTitles.append(key['properties']['title'])

# title = eqData['metadata']
# fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title['title'],
#                      color=mags,
#                      color_continuous_scale='plasma',
#                      labels={'color': 'Magnitude'},
#                      projection='natural earth',
#                      hover_name=eqTitles,
# )
# fig.show()

# 16.9
path = Path('C:\\Users\\marse\\OneDrive\\Рабочий стол\\Projects\\dataWork\\eqData\\world_fires_1_day.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)

header = next(reader)
latsIndex, lonsIndex = 0, 0 
for index, name in enumerate(header):
    if name == 'latitude': latsIndex = index
for index, name in enumerate(header):
    if name == 'longitude': lonsIndex = index

lats, lons, brights = [], [], []
for r in reader:
    lats.append(float(r[latsIndex]))
    lons.append(float(r[lonsIndex]))
    brights.append(float(r[2]))

fig = px.scatter_geo(lat=lats, lon=lons, size=brights, title='Пожары',
                     color=brights,
                     color_continuous_scale='hot',
                     labels={'color': 'Magnitude'},
                     projection='natural earth',
)
fig.show()
