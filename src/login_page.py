from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc


login_layout = html.Div(
    [
        # dcc.Location(id="page", refresh=False),
        # html.H2("Dash Login Page"),
        html.Div(
            [
                html.H1("Login"),
                dbc.Row(
                    [
                        html.Label(
                            "User Name:*",
                            style={
                                "width": "150px",
                                "display": "inline-block",
                            },
                        ),
                        dcc.Input(
                            id="username-input",
                            type="text",
                            placeholder="User Name",
                            style={
                                "width": "300px",
                                "display": "inline-block",
                                "height": 30,
                                # "border-color": "red",
                            },
                        ),
                    ]
                ),
                # html.Hr(),
                dbc.Row(
                    [
                        html.Label(
                            "Password:*",
                            style={
                                "width": "150px",
                                "display": "inline-block",
                            },
                        ),
                        dcc.Input(
                            id="password-input",
                            type="password",
                            placeholder="Password",
                            style={
                                "width": "300px",
                                "display": "inline-block",
                                "height": 30,
                                # "border-color": "red",
                            },
                        ),
                    ]
                ),
                # dcc.Input(
                #     id="username-input", type="text", placeholder="Enter your username"
                # ),
                # dcc.Input(
                #     id="password-input",
                #     type="password",
                #     placeholder="Enter your password",
                # ),
                html.Button("Login", id="login-button"),
                html.Div(id="login-status"),
            ],
            style={
                "position": "absolute",
                "left": "50%",
                "top": "40%",
                "transform": "translate(-50%, -50%)",
                "text-align": "center",
                "width": "40%",
                "font-size": "24px",  # Adjust the font size as needed
                "box-shadow": "0 0 20px rgba(0, 0, 0, 0.5)",  # Add a box-shadow for projection effect
                "padding": "20px",
            },
        ),
    ]
)


def login_page():
    print("login_page")
    return login_layout
