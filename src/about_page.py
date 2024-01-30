# Callback to update the page content based on the URL
import json
import pandas as pd
from dash import dcc, html
import dash_bootstrap_components as dbc
from app2 import gapMinder
from dash.dependencies import Input, Output


from dash_table import DataTable

with open("about.json", "r") as file:
    table = json.load(file)


continent_options = [
    {"label": continent, "value": continent}
    for continent in gapMinder["continent"].unique()
]
country_options = [
    {"label": country, "value": country} for country in gapMinder["country"].unique()
]
pop_min = gapMinder["pop"].min()
pop_max = gapMinder["pop"].max()
exp_min = gapMinder["lifeExp"].min()
exp_max = gapMinder["lifeExp"].max()

about_layout = html.Div(
    [
        html.H3("Introduction to GapMinder", style={"textAlign": "center"}),
        html.P(table["main_intro"]),
        html.Li(table["first_point"]),
        html.Li(table["second_point"]),
        html.Label("Show no of rows"),
        dcc.Dropdown(
            id="page-size-dropdown",
            options=[
                {"label": "10", "value": 10},
                {"label": "20", "value": 20},
                {"label": "30", "value": 30},
            ],
            value=10,
            style={
                "width": "50%",
            },
        ),
        DataTable(
            id="data_table",
            columns=[
                {"name": "continent", "id": "continent"},
                {"name": "country", "id": "country"},
                {"name": "Population", "id": "pop"},
                {"name": "Life expectancy", "id": "lifeExp"}
                #  for col in gapMinder.columns
            ],
            data=gapMinder.to_dict("records"),
            page_size=10,
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Dropdown(
                        id="continent_dropdown",
                        options=continent_options,
                        value=continent_options[0]["value"],
                    ),
                    style={"width": 300},
                ),
                dbc.Col(
                    dcc.Dropdown(
                        id="country_dropdown",
                        options=country_options,
                        value=[country_options[0]["value"]],
                        multi=True,
                    ),
                    style={"width": 300},
                ),
                dbc.Col(
                    dcc.Slider(
                        id="pop_slider",
                        min=pop_min,
                        max=pop_max,
                        # step=10000000,
                        # marks={i: str(i) for i in range(11)},
                        value=(pop_max - pop_min) / 2,
                    ),
                    style={"width": 300},
                ),
                dbc.Col(
                    dcc.Slider(
                        id="exp_slider",
                        min=exp_min,
                        max=exp_max,
                        # step = ,
                        # marks={i: str(i) for i in range(11)},
                        value=60,
                    ),
                    style={"width": 300},
                ),
            ],
            style={
                "justify-content": "space-between",
                "display": "flex",
                "flex": 1,
                # "margin-right": "20px"
                # "align-items": "center",
            },
        ),
        html.Button("Download CSV", id="btn_download_csv"),
        dcc.Download(id="download_csv"),
    ]
)


def about_page():
    return about_layout
