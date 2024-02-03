import dash
import pandas as pd
from app_auth import server as flask_app
from dash import dcc, html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, server=flask_app, suppress_callback_exceptions=True)


# gapMinder_raw = pd.read_csv(
#     "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
# )
gapMinder_raw = pd.read_csv("gapminderDataFiveYear.csv")
# print(gapMinder.columns)
gapMinder = gapMinder_raw[
    ["continent", "country", "pop", "lifeExp", "gdpPercap", "year"]
]


# base_layout = html.Div(
#     children=[
#         html.Div(
#             [
#                 dbc.Row(
#                     [
#                         dbc.Col(
#                             children=[
#                                 html.Img(
#                                     src="https://www.tigeranalytics.com/wp-content/uploads/2023/09/TA-Logo-resized-for-website_.png",  # Replace with your logo URL
#                                     style={
#                                         "height": "50px",
#                                         "width": "120px",
#                                         "backgroundColor": "white",
#                                     },  # Adjust size as needed
#                                 )
#                             ],
#                             style={"width": 200},
#                         ),
#                         #     dbc.Col(
#                         #         children=[
#                         #             dcc.Link(
#                         #                 "About",
#                         #                 href="/page-1",
#                         #                 style={
#                         #                     "color": "white",
#                         #                     # "textDecoration": "underline",
#                         #                     "float": "left",
#                         #                     "width": 70,
#                         #                 },
#                         #             ),  # Link to Page 1
#                         #             # html.Span(" | "),
#                         #             dcc.Link(
#                         #                 "Input field",
#                         #                 href="/page-2",
#                         #                 style={
#                         #                     "color": "white",
#                         #                     # "textDecoration": "underline",
#                         #                     # "text-align": "center",
#                         #                     "display": "inline-flex",
#                         #                     "width": 85,
#                         #                 },
#                         #             ),  # Link to Page 2
#                         #             # html.Span(" | "),
#                         #             dcc.Link(
#                         #                 "Simulation",
#                         #                 href="/page-3",
#                         #                 style={
#                         #                     "color": "white",
#                         #                     # "textDecoration": "underline",
#                         #                     # "float": "center",
#                         #                     "width": 80,
#                         #                 },
#                         #             ),  # Link to Page 3
#                         #             dcc.Link(
#                         #                 "Logout",
#                         #                 href="/page-3",
#                         #                 style={
#                         #                     "color": "white",
#                         #                     # "textDecoration": "underline",
#                         #                     "float": "right",
#                         #                 },
#                         #             ),  # Link to Page 3
#                         #         ],
#                         #         style={
#                         #             "width": 300,
#                         #             "position": "absolute",
#                         #             "top": 20,
#                         #             "right": 30,
#                         #             "justify-content": "space-between",
#                         #         },
#                         #     ),
#                     ],
#                     style={"backgroundColor": "blue", "height": 50},
#                 ),
#                 dbc.Row(
#                     id="page-content", children=login_layout
#                 ),  # Placeholder for the page content
#             ],
#         ),
#     ],
#     id="main_layout",
# )
