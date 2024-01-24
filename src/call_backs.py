from dash.dependencies import Input, Output
import pandas as pd
from app2 import app, gapMinder
from dash.exceptions import PreventUpdate

from about_page import about_page
from input_page import input_page
from dash import dcc, html


def csv_download():
    @app.callback(
        Output("download_csv", "data"),
        [Input("btn_download_csv", "n_clicks"), Input("data_table", "data")],
    )
    def download_csv(n_clicks, data):
        if n_clicks is not None:
            df = pd.DataFrame(data)
            csv_string = df.to_csv(index=False, encoding="utf-8")
            return dict(content=csv_string, filename="data.csv")


##########
def dataframe_update():
    @app.callback(
        Output("data_table", "data"),
        [
            Input("continent_dropdown", "value"),
            Input("country_dropdown", "value"),
            Input("pop_slider", "value"),
            Input("exp_slider", "value"),
        ],
    )
    def update_dataframe(value_continent, value_country, value_pop, value_exp):
        df = gapMinder[
            (gapMinder["continent"] == value_continent)
            & (gapMinder["country"].isin(value_country))
        ]
        df = df[(df["pop"] <= value_pop) & (df["lifeExp"] <= value_exp)]
        return df.to_dict("records")


def list_country():
    @app.callback(
        Output("country_dropdown", "options"),
        [Input("continent_dropdown", "value")],
    )
    def country_list(value_continent):
        df = gapMinder[gapMinder["continent"] == value_continent]
        return [
            {"label": country, "value": country} for country in df["country"].unique()
        ]


# Sample callback using the generated DataTable
def pagesize_update():
    @app.callback(
        Output("data_table", "page_size"),
        [Input("page-size-dropdown", "value")],
    )
    def update_page_size(page_size):
        if page_size is None:
            raise PreventUpdate
        return page_size


# # Callback to update the page content based on the URL
def page_Selection():
    @app.callback(Output("page-content", "children"), [Input("url", "pathname")])
    def display_page(pathname):
        if pathname == "/page-1":
            return about_page()
        elif pathname == "/page-2":
            return input_page()
        elif pathname == "/page-3":
            return html.Div(
                [html.H3("Simulation"), html.P("This is content for Page 3.")]
            )
        else:
            return about_page()


# # Registering all callbacks
def register_callbacks(app):
    page_Selection()
    pagesize_update()
    list_country()
    dataframe_update()
    csv_download()
