from dash import dcc, html
import dash_bootstrap_components as dbc
from login_page import login_layout


def logout_page():
    print("logout_page")
    return logout_layout


logout_layout = (
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
                ],
                style={"backgroundColor": "blue", "height": 50},
            ),
            html.Div(
                [
                    html.H3("Successfully logged out"),
                    # html.Button(id="goto_home_button", style={"font-size": "24px"}),
                    dcc.Link(html.Button("Go to login page"), href="/"),
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
            # dbc.Row(
            #     id="page-content", children=login_layout
            # ),  # Placeholder for the page content
        ],
    ),
)


def log_after_logout():
    return login_after_logout


login_after_logout = (
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
                ],
                style={"backgroundColor": "blue", "height": 50},
            ),
            dbc.Row(
                id="page-content", children=login_layout
            ),  # Placeholder for the page content
        ],
    ),
)
