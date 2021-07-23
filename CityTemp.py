import pandas as pd
import pycountry
import plotly.express as px

def partial_name(c_name, key_list):
    if c_name == 'US':
        return 'United States'
    for x in key_list:
        if (c_name[0:3] == x[0:3]) | (c_name[-8:] == x[-8:]):
            return x

countries = {}
for country in pycountry.countries:
    countries[country.name] = country.alpha_3

csv_path=".\\archive\city_temperature.csv"
df = pd.read_csv(csv_path)

df['Country2'] = [partial_name(x2,list(countries.keys())) for x2 in df['Country']]

df['alpha_iso'] = [countries.get(country, 'na') for country in df["Country2"]]

df = df[df['alpha_iso'] != 'na']

df = df.drop(labels = "Country", axis = 1)

df = df[df['AvgTemperature'] > -99].reset_index(drop = True)

df=

df_uni_cnty = df.drop_duplicates(subset = "Country2")

fig = px.choropleth(df_uni_cnty, locations="alpha_iso",
                    color="AvgTemperature", # lifeExp is a column of gapminder
                    hover_name="Country2", # column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plasma
                    animation_frame = "Year")

fig.write_image("./test.svg")


