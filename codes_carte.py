import pandas as pd
import numpy as np

url = '/home/legrand/Documents/Mouettes_Savantes/2024/donnees/All_temperatures.csv'
df = pd.read_csv(url)


url = '/home/legrand/Documents/Mouettes_Savantes/2024/donnees/Stations_id.csv'
coord = pd.read_csv(url)

coord.head()

import plotly.express as px
fig = px.scatter_mapbox(coord,
                        lat="lat",
                        lon="lon",
                        hover_name="STANAME",
                        color=moyenne, # à définir !
                        size = variance, # à définir !
                        height=800,
                        width=800)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
