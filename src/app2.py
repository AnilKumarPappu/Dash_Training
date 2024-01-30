import dash
import pandas as pd

app = dash.Dash(__name__, suppress_callback_exceptions=True)


# gapMinder_raw = pd.read_csv(
#     "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
# )
gapMinder_raw = pd.read_csv("/home/anil_tiger/Dash_training/gapminderDataFiveYear.csv")
# print(gapMinder.columns)
gapMinder = gapMinder_raw[
    ["continent", "country", "pop", "lifeExp", "gdpPercap", "year"]
]
