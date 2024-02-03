import json
import pandas as pd
from dash_table import DataTable
from dash import dcc, html
import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


from call_backs import register_callbacks
from app2 import app
from login_page import login_layout

# from app2 import gapMinder

# app = dash.Dash(__name__, suppress_callback_exceptions=True)

server = app.server

with open("about.json", "r") as file:
    table = json.load(file)

# app = dash.Dash(__name__)
# Define the navigation bar layout
app.layout = html.Div(
    [
        dcc.Store(id="lat_store", data=56),
        dcc.Store(id="long_store", data=45),
        dcc.Store(id="data_store", data="year"),
        dcc.Store(id="country_store", data="India"),
        dcc.Store(id="valid_user", data=0),
        dcc.Location(id="url", refresh=False),  # Location component to track the URL
        # html.H1("aklsdjflk"),
        dbc.Row(
            children=[
                html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    children=[
                                        html.Img(
                                            src="https://www.tigeranalytics.com/wp-content/uploads/2023/09/TA-Logo-resized-for-website_.png",  # Replace with your logo URL
                                            style={
                                                "height": "50px",
                                                "width": "120px",
                                                "backgroundColor": "white",
                                            },  # Adjust size as needed
                                        )
                                    ],
                                    style={"width": 200},
                                ),
                                #     dbc.Col(
                                #         children=[
                                #             dcc.Link(
                                #                 "About",
                                #                 href="/page-1",
                                #                 style={
                                #                     "color": "white",
                                #                     # "textDecoration": "underline",
                                #                     "float": "left",
                                #                     "width": 70,
                                #                 },
                                #             ),  # Link to Page 1
                                #             # html.Span(" | "),
                                #             dcc.Link(
                                #                 "Input field",
                                #                 href="/page-2",
                                #                 style={
                                #                     "color": "white",
                                #                     # "textDecoration": "underline",
                                #                     # "text-align": "center",
                                #                     "display": "inline-flex",
                                #                     "width": 85,
                                #                 },
                                #             ),  # Link to Page 2
                                #             # html.Span(" | "),
                                #             dcc.Link(
                                #                 "Simulation",
                                #                 href="/page-3",
                                #                 style={
                                #                     "color": "white",
                                #                     # "textDecoration": "underline",
                                #                     # "float": "center",
                                #                     "width": 80,
                                #                 },
                                #             ),  # Link to Page 3
                                #             dcc.Link(
                                #                 "Logout",
                                #                 href="/page-3",
                                #                 style={
                                #                     "color": "white",
                                #                     # "textDecoration": "underline",
                                #                     "float": "right",
                                #                 },
                                #             ),  # Link to Page 3
                                #         ],
                                #         style={
                                #             "width": 300,
                                #             "position": "absolute",
                                #             "top": 20,
                                #             "right": 30,
                                #             "justify-content": "space-between",
                                #         },
                                #     ),
                            ],
                            style={"backgroundColor": "blue", "height": 50},
                        ),
                        dbc.Row(
                            id="page-content", children=login_layout
                        ),  # Placeholder for the page content
                    ],
                ),
            ],
            id="main_layout",
        )
        # html.Div(
        #     [
        #         html.Div(id="display-store-1"),
        #         # html.Div(id='display-store-2'),
        #         # html.Div(id='display-store-3'),
        #     ]
        # ),
    ]
)


# app.layout.children[7].children[0].children = [
#     html.Div("Stored Data for Store 2: ", style={"fontWeight": "bold"}),
#     html.Pre(id="display-store-1-html"),
# ]
# print(app.layout["lat_store"].data)
# app.layout["display-store-1-html"].children = f'{app.layout["lat_store"]}'


# @app.callback(Output("display-store-1-html", "children"), Input("lat_store", "data"))
# def display_lat_store(data):
#     return f"Stored Data for lat_store: {data}"


# ################################
register_callbacks(app)

# ######################################
if __name__ == "__main__":
    app.run_server(debug=True, port=8051)
