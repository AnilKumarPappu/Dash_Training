from dash import dcc, html
import dash_bootstrap_components as dbc


input_layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H3("User Input"),
                        html.Hr(style={"border-width": "3px"}),
                        html.Div(
                            [
                                dbc.Row(
                                    [
                                        html.Label(
                                            "Latitude:*",
                                            style={
                                                "width": "150px",
                                                "display": "inline-block",
                                            },
                                        ),
                                        dcc.Input(
                                            id="input_latitude",
                                            type="number",
                                            placeholder="input latitude",
                                            style={
                                                "width": "300px",
                                                "display": "inline-block",
                                                "height": 30,
                                                "border-color": "red",
                                            },
                                        ),
                                    ]
                                ),
                                html.Hr(),
                                dbc.Row(
                                    [
                                        html.Label(
                                            "Longitude:*",
                                            style={
                                                "width": "150px",
                                                "display": "inline-block",
                                            },
                                        ),
                                        dcc.Input(
                                            id="input_longitude",
                                            type="number",
                                            placeholder="input longitude",
                                            style={
                                                "width": "300px",
                                                "display": "inline-block",
                                                "height": 30,
                                                "border-color": "red",
                                            },
                                        ),
                                    ]
                                ),
                                html.Hr(),
                                dbc.Row(
                                    [
                                        html.Label(
                                            "State:*",
                                            style={
                                                "width": "150px",
                                                "display": "inline-block",
                                            },
                                        ),
                                        dcc.Input(
                                            id="input_data",
                                            type="text",
                                            placeholder="input country or year",
                                            style={
                                                "width": "300px",
                                                "display": "inline-block",
                                                "height": 30,
                                                "border-color": "red",
                                            },
                                        ),
                                    ]
                                ),
                                html.Hr(),
                                dbc.Row(
                                    [
                                        html.Label(
                                            "Country:*",
                                            style={
                                                "width": "150px",
                                                "display": "inline-block",
                                            },
                                        ),
                                        dcc.Input(
                                            id="input_country",
                                            type="text",
                                            placeholder="input country",
                                            style={
                                                "width": "300px",
                                                "display": "inline-block",
                                                "height": 30,
                                                "border-color": "red",
                                            },
                                        ),
                                    ]
                                ),
                                html.Hr(),
                            ],
                            style={
                                # "display": "flex",
                                # "flex-direction": "column",
                                # "width": 20,
                            },
                        ),
                    ],
                    style={"width": "50%"},
                ),
                dbc.Col(
                    [
                        html.H3("Calculated Output"),
                        html.Hr(style={"border-width": "1px"}),
                        html.Div(id="output_gen_display"),
                    ],
                    style={"width": "50%"},
                ),
            ],
            style={
                "justify-content": "space-between",
                "display": "flex",
                "flex": 1,
            },
        ),
        html.Button(
            "Simulate",
            id="simulate-button",
            style={"margin": "auto", "display": "block"},
        ),
    ]
)


def input_page():
    return input_layout
