from dash import dcc, html
import dash_bootstrap_components as dbc
import dash_leaflet as dl

# from app import app

simulation_layout = html.Div(
    [
        dl.Map(
            dl.TileLayer(),
            id="map-output",
            center=[20, 20],  # default values
            zoom=6,
            style={
                "height": 400,
                "width": "95%",
                "margin": "auto",
                "marginTop": "30px",
            },
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            children=[
                                # html.H1("Text Box Example"),
                                html.Div("User provided fields"),
                            ],
                            style={
                                "border": "2px solid #0074D9",
                                "padding": "10px",
                                "margin": "10px",
                                "background-color": "blue",
                                "color": "white",
                                "text-align": "center",
                            },
                        ),
                        html.Div(
                            [
                                dbc.Row(
                                    [
                                        html.Label(
                                            "Latitude:",
                                            style={
                                                "width": "150px",
                                                "display": "inline-block",
                                                "text-align": "center",
                                            },
                                        ),
                                        html.Div(
                                            id="lat_display",
                                            style={
                                                "background-color": "lightgray",
                                                "width": 300,
                                                "display": "inline-block",
                                            },
                                        ),
                                    ]
                                ),
                                html.Hr(),
                                dbc.Row(
                                    [
                                        html.Label(
                                            "Longitude:",
                                            style={
                                                "width": "150px",
                                                "display": "inline-block",
                                                "text-align": "center",
                                            },
                                        ),
                                        html.Div(
                                            id="log_display",
                                            style={
                                                "width": "300px",
                                                "display": "inline-block",
                                                "background-color": "lightgray",
                                            },
                                        ),
                                    ]
                                ),
                                html.Hr(),
                                dbc.Row(
                                    [
                                        html.Label(
                                            "State:",
                                            style={
                                                "width": "150px",
                                                "display": "inline-block",
                                                "text-align": "center",
                                            },
                                        ),
                                        html.Div(
                                            id="data_display",
                                            style={
                                                "width": "300px",
                                                "display": "inline-block",
                                                "background-color": "lightgray",
                                            },
                                        ),
                                    ]
                                ),
                                html.Hr(),
                                dbc.Row(
                                    [
                                        html.Label(
                                            "Country:",
                                            style={
                                                "width": "150px",
                                                "display": "inline-block",
                                                "text-align": "center",
                                            },
                                        ),
                                        html.Div(
                                            id="country_display",
                                            style={
                                                "width": "300px",
                                                "display": "inline-block",
                                                "background-color": "lightgray",
                                            },
                                        ),
                                    ]
                                ),
                                html.Hr(),
                            ]
                        ),
                    ],
                    # style={"width": "50%"},
                    style={
                        "display": "inline-block",
                        "width": "49%",
                    },
                ),
                dbc.Col(
                    [
                        html.Div(
                            children=[
                                # html.H1("Text Box Example"),
                                html.Div("Country Data"),
                            ],
                            style={
                                "border": "2px solid #0074D9",
                                "padding": "10px",
                                "margin": "10px",
                                "background-color": "blue",
                                "color": "white",
                                "text-align": "center",
                            },
                        ),
                        html.Div(
                            [
                                dbc.Row(
                                    [
                                        html.Label(
                                            "Latest GDP",
                                            style={
                                                "width": "150px",
                                                "display": "inline-block",
                                                "text-align": "center",
                                            },
                                        ),
                                        html.Div(
                                            id="gdp_display",
                                            style={
                                                "background-color": "lightgray",
                                                "width": 300,
                                                "display": "inline-block",
                                            },
                                        ),
                                    ]
                                ),
                                html.Hr(),
                                dbc.Row(
                                    [
                                        html.Label(
                                            "Latest Population",
                                            style={
                                                "width": "150px",
                                                "display": "inline-block",
                                                "text-align": "center",
                                            },
                                        ),
                                        html.Div(
                                            id="pop_display",
                                            style={
                                                "background-color": "lightgray",
                                                "width": 300,
                                                "display": "inline-block",
                                            },
                                        ),
                                    ]
                                ),
                                html.Hr(),
                                dbc.Row(
                                    [
                                        html.Label(
                                            "Average Life Expectancy",
                                            style={
                                                "width": "150px",
                                                "display": "inline-block",
                                                "text-align": "center",
                                            },
                                        ),
                                        html.Div(
                                            id="life_display",
                                            style={
                                                "background-color": "lightgray",
                                                "width": 300,
                                                "display": "inline-block",
                                            },
                                        ),
                                    ]
                                ),
                            ]
                        ),
                    ],
                    style={
                        "display": "inline-block",
                        "width": "49%",
                    },
                ),
            ],
            style={
                "justify-content": "space-between",
                "display": "flex",
                "flex": 1,
            },
        ),
        dcc.Graph(id="bar_plot_pop"),
        dcc.Graph(id="bar_plot_gdp"),
    ],
)


def simulation_page():
    return simulation_layout
