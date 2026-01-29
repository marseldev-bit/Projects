from pathlib import Path
import json
import plotly.express as px

path = Path('C:\\Users\\marse\\OneDrive\\Рабочий стол\\Projects\\dataWork\\eqData\\eq_data_1_day_m1.geojson')
eqData = json.loads(path.read_text())

# path = Path('C:\\Users\\marse\\OneDrive\\Рабочий стол\\Projects\\dataWork\\eqData\\readable_eq_data.geojson')
# path.write_text(json.dumps(eqData, indent=4))

eqDicts = eqData['features']

mags, lons, lats, eqTitles = [], [], [], []
for key in eqDicts:
    mags.append(key['properties']['mag'])
    lons.append(key['geometry']['coordinates'][0])
    lats.append(key['geometry']['coordinates'][1])
    eqTitles.append(key['properties']['title'])

fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title='Global Earthquakes',
                     color=mags,
                     color_continuous_scale='plasma',
                     labels={'color': 'Magnitude'},
                     projection='natural earth',
                     hover_name=eqTitles,
)
fig.show()