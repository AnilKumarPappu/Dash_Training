import json
import pandas as pd
from dash_table import DataTable
from dash import dcc, html
import dash
import dash_bootstrap_components as dbc

from dash.exceptions import PreventUpdate

# from about_page import about_page
from dash.dependencies import Input, Output

# import urllib

# from call_backs import register_callbacks
# from app import app
app = dash.Dash(__name__, suppress_callback_exceptions=True)

server = app.server

gapMinder_raw = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
)
# print(gapMinder.columns)
gapMinder = gapMinder_raw[["continent", "country", "pop", "lifeExp"]]
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
with open("about.json", "r") as file:
    table = json.load(file)

# app = dash.Dash(__name__)
# Define the navigation bar layout
app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),  # Location component to track the URL
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
                dbc.Col(
                    children=[
                        dcc.Link(
                            "About",
                            href="/page-1",
                            style={
                                "color": "white",
                                # "textDecoration": "underline",
                                "float": "left",
                                "width": 70,
                            },
                        ),  # Link to Page 1
                        # html.Span(" | "),
                        dcc.Link(
                            "Input field",
                            href="/page-2",
                            style={
                                "color": "white",
                                # "textDecoration": "underline",
                                # "text-align": "center",
                                "display": "inline-flex",
                                "width": 85,
                            },
                        ),  # Link to Page 2
                        # html.Span(" | "),
                        dcc.Link(
                            "Simulation",
                            href="/page-3",
                            style={
                                "color": "white",
                                # "textDecoration": "underline",
                                # "float": "center",
                                "width": 80,
                            },
                        ),  # Link to Page 3
                        dcc.Link(
                            "Logout",
                            href="/page-3",
                            style={
                                "color": "white",
                                # "textDecoration": "underline",
                                "float": "right",
                            },
                        ),  # Link to Page 3
                    ],
                    style={
                        "width": 300,
                        "position": "absolute",
                        "top": 20,
                        "right": 30,
                        "justify-content": "space-between",
                    },
                ),
            ],
            style={"backgroundColor": "blue", "height": 50},
        ),
        dbc.Row(id="page-content"),  # Placeholder for the page content
    ]
)

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


####################
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


@app.callback(
    Output("country_dropdown", "options"),
    [Input("continent_dropdown", "value")],
)
def country_list(value_continent):
    df = gapMinder[gapMinder["continent"] == value_continent]
    return [{"label": country, "value": country} for country in df["country"].unique()]


################################
# register_callbacks(app)


# Sample callback using the generated DataTable
# def update_output_div():
@app.callback(
    Output("data_table", "page_size"),
    [Input("page-size-dropdown", "value")],
)
def update_page_size(page_size):
    if page_size is None:
        raise PreventUpdate
    return page_size


# # Callback to update the page content based on the URL
# def page_Selection():
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/page-1":
        return about_page()
    elif pathname == "/page-2":
        return html.Div([html.H3("Input field"), html.P("This is content for Page 2.")])
    elif pathname == "/page-3":
        return html.Div([html.H3("Simulation"), html.P("This is content for Page 3.")])
    else:
        return about_page()
        # return html.Div(
        #     [
        #         html.H3("404 - Page not found"),
        #         html.P("The requested URL was not found on the server."),
        #     ]
        # )


######################################
if __name__ == "__main__":
    app.run_server(debug=True)
