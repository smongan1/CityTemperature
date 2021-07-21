import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from urllib.request import urlopen
import json
import pycountry
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
    
countries = {}
for country in pycountry.countries:
    countries[country.name] = country.alpha_3

import plotly.express as px

csv_path="C:\\Users\smong\Downloads\\archive\city_temperature.csv"
df = pd.read_csv(csv_path)
df['alpha_iso'] = [countries.get(country, 'Unknown code') for country in df["Country"]]

fig = px.choropleth(df[df["Country"] in df["Country"].unique()], locations="Country",
                    color="AvgTemperature", # lifeExp is a column of gapminder
                    hover_name="Country", # column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plasma)
fig.show()