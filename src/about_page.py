# # Callback to update the page content based on the URL
# import json
# import pandas as pd
# from dash import dcc, html
# import dash_bootstrap_components as dbc

# from dash.dependencies import Input, Output


# # @app.callback(Output("page-content", "children"), [Input("url", "pathname")])
# # def display_page(pathname):
# #     if pathname == "/page-1":
# #         return html.Div([html.H3("Page 1"), html.P("This is content for Page 1.")])
# #     elif pathname == "/page-2":
# #         return html.Div([html.H3("Page 2"), html.P("This is content for Page 2.")])
# #     elif pathname == "/page-3":
# #         return html.Div([html.H3("Page 3"), html.P("This is content for Page 3.")])
# #     else:
# #         return html.Div(
# #             [
# #                 html.H3("404 - Page not found"),
# #                 html.P("The requested URL was not found on the server."),
# #             ]
# #         )
# from dash_table import DataTable

# with open("about.json", "r") as file:
#     table = json.load(file)

# gapMinder = pd.read_csv(
#     "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
# )
# # print(gapMinder.columns)
# gapMinder = gapMinder[["continent", "country", "pop", "lifeExp"]]


# def about_page():
#     about_layout = html.Div(
#         [
#             html.H3("Introduction to GapMinder", style={"textAlign": "center"}),
#             html.P(table["main_intro"]),
#             html.Li(table["first_point"]),
#             html.Li(table["second_point"]),
#             html.Label("Show no of rows"),
#             dcc.Dropdown(
#                 id="page-size-dropdown",
#                 options=[
#                     {"label": "10", "value": 10},
#                     {"label": "20", "value": 20},
#                     {"label": "30", "value": 30},
#                 ],
#                 value=10,
#                 style={
#                     "width": "50%",
#                 },
#             ),
#             DataTable(
#                 id="data_table",
#                 columns=[
#                     {"name": "continent", "id": "continent"},
#                     {"name": "country", "id": "country"},
#                     {"name": "Population", "id": "pop"},
#                     {"name": "Life expectancy", "id": "lifeExp"}
#                     #  for col in gapMinder.columns
#                 ],
#                 data=gapMinder.to_dict("records"),
#                 page_size=10,
#             ),
#         ]
#     )
#     return about_layout
