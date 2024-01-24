import dash
import pandas as pd

app = dash.Dash(__name__, suppress_callback_exceptions=True)


gapMinder_raw = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
)
# print(gapMinder.columns)
gapMinder = gapMinder_raw[["continent", "country", "pop", "lifeExp"]]