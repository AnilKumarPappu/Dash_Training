from dash.dependencies import Input, Output, State
import pandas as pd
from app2 import app, gapMinder
from dash.exceptions import PreventUpdate
from app_auth import server as flask_app

from views.about_page import about_page
from views.input_page import input_page
from views.log_out import logout_page, log_after_logout
from views.simulation_page import simulation_page
from views.login_page import login_page
import plotly.express as px
import dash_leaflet as dl

from sub_main import sub_main


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
    @app.callback(
        Output("page-content", "children"),
        [Input("url", "pathname")],
        [State("valid_user", "data")],
    )
    def display_page(pathname, valid_user):
        print("display_page")

        if pathname == "/page-1":
            return about_page()
        elif pathname == "/page-2":
            return input_page()
        elif pathname == "/page-3":
            return simulation_page()
        elif pathname == "/page-4":
            raise PreventUpdate
        elif valid_user == 1:
            return about_page()
        else:
            return login_page()


# # Callback to update the page content based on the URL
def page_selection_logout():
    @app.callback(
        Output("main_layout", "children", allow_duplicate=True),
        [Input("url", "pathname")],
        [State("valid_user", "data")],
        prevent_initial_call=True,
    )
    def display_page_logout(pathname, valid_user):
        print("display_page_logout")

        # if pathname == "/page-1":
        #     return about_page()
        # elif pathname == "/page-2":
        #     return input_page()
        # elif pathname == "/page-3":
        #     return simulation_page()
        if pathname == "/page-4":
            return logout_page()
        elif valid_user == 0:
            return log_after_logout()

        else:
            raise PreventUpdate


# output generated msg at input page
def out_gen():
    @app.callback(
        Output("output_gen_display", "children"), [Input("simulate-button", "n_clicks")]
    )
    def output_gen(clicks):
        if clicks is None:
            raise PreventUpdate
        return "Output generated"


# callback for simulation page
def simulation_input():
    @app.callback(
        [
            Output("lat_store", "data"),
            Output("long_store", "data"),
            Output("data_store", "data"),
            Output("country_store", "data"),
        ],
        [Input("simulate-button", "n_clicks")],
        [
            State("input_latitude", "value"),
            State("input_longitude", "value"),
            State("input_data", "value"),
            State("input_country", "value"),
        ],
    )
    def input_simulation(n_clicks, latitude, longitude, state, country):
        if (state != "country") & (state != "year"):
            raise PreventUpdate
        country_list = gapMinder["country"].unique().tolist()
        if country not in country_list:
            raise PreventUpdate
        out_1 = latitude
        out_2 = longitude
        out_3 = state
        out_4 = country
        return out_1, out_2, out_3, out_4


# call back to display input
def display_input():
    @app.callback(
        Output("lat_display", "children"),
        Output("log_display", "children"),
        Output("data_display", "children"),
        Output("country_display", "children"),
        [
            Input("lat_store", "data"),
            Input("long_store", "data"),
            Input("data_store", "data"),
            Input("country_store", "data"),
        ],
    )
    def input_display(lat, log, state, country):
        return lat, log, state, country


# map for simulation
def map_simulation():
    @app.callback(
        Output("map-output", "children"),
        Output("map-output", "center"),
        [Input("lat_store", "data"), Input("long_store", "data")],
    )
    def simulation_map(latitude, longitude):
        if (latitude is None) & (longitude is None):
            raise PreventUpdate
        # print(type(latitude))
        marker = dl.Marker(
            position=[latitude, longitude],
            children=[dl.Tooltip(f"Latitude: {latitude}, Longitude: {longitude}")],
        )
        center = [latitude, longitude]
        # print(center)
        # print(marker)
        return [dl.TileLayer(), marker], center


# display country information
def info_country():
    @app.callback(
        Output("gdp_display", "children"),
        Output("pop_display", "children"),
        Output("life_display", "children"),
        [Input("country_store", "data")],
    )
    def country_info(country):
        gdp_country = gapMinder[gapMinder["country"] == country]
        gdp = gdp_country[gdp_country["year"] == gdp_country["year"].max()]["gdpPercap"]

        pop_country = gapMinder[gapMinder["country"] == country]
        pop = pop_country[pop_country["year"] == pop_country["year"].max()]["pop"]

        life = gapMinder[gapMinder["country"] == country]["lifeExp"].mean()
        return gdp, pop, life


# bar plot for pop on year for a country
def barplot_pop():
    @app.callback(
        Output("bar_plot_pop", "figure"),
        [Input("country_store", "data")],
    )
    def update_bar_plot(selected_country):
        filtered_gapMinder = gapMinder[gapMinder["country"] == selected_country]
        fig = px.bar(
            filtered_gapMinder,
            x="year",
            y="pop",
            color="lifeExp",
            labels={"pop": "Population", "lifeExp": "Life Expectancy"},
            title=f"Bar Plot for {selected_country}",
        )
        return fig


# bar plot for GDP on year or countries
def barplot_GDP():
    @app.callback(
        Output("bar_plot_gdp", "figure"),
        [Input("data_store", "data")],
    )
    def update_bar_plot(selected_state):
        X = selected_state
        # filtered_gapMinder = gapMinder[gapMinder["country"] == selected_country]
        fig = px.bar(
            gapMinder,
            x=X,
            y="gdpPercap",
            labels={"gdpPercap": "GDP per capita"},
            title=f"GDP per capita over {selected_state}",
        )
        # fig.update_layout(barmode="stack")
        return fig


# flask login
def login_flask():
    # Callback to handle login button click
    @app.callback(
        [
            Output("main_layout", "children", allow_duplicate=True),
            Output("valid_user", "data", allow_duplicate=True),
        ],
        [Input("login-button", "n_clicks")],
        [State("username-input", "value"), State("password-input", "value")],
        prevent_initial_call=True,
        # allow_duplicate=True,
    )
    def handle_login(n_clicks, username, password):
        print("login_flask")
        print(n_clicks)
        if n_clicks is None:
            print("into prevent update")
            raise PreventUpdate
        elif n_clicks and username and password:
            # Send login request to the Flask server
            print("before login")
            response = flask_app.test_client().post(
                "/login",
                data={"username": username, "password": password},
                follow_redirects=True,
            )
            print(response)
            if response.status_code == 200:
                # return f"Login successful! Welcome, {current_user.username}!"
                return sub_main(), 1
            else:
                return "Login failed. Please check your credentials.", 0
        else:
            print("into else")
            return "username or password are not entered", 0


def logout_flask():
    @app.callback(
        Output("valid_user", "data", allow_duplicate=True),
        [Input("url", "pathname")],
        prevent_initial_call=True,
        allow_duplicate=True,
    )
    def logout_user(pathname):
        if pathname == "/page-4":
            return 0
        else:
            raise PreventUpdate


def goto_home_page():
    @app.callback(
        Output("url", "pathname"),
        [Input("goto_home_button", "n_clicks")],
        prevent_initial_call=True,
    )
    def go_to_base_link(n_clicks):
        if n_clicks:
            print("go to home page")
            return "/"
        else:
            # If the button hasn't been clicked, keep the current URL
            raise PreventUpdate


# # Registering all callbacks
def register_callbacks(app):
    page_Selection()
    pagesize_update()
    list_country()
    dataframe_update()
    csv_download()
    simulation_input()
    # assig()
    map_simulation()
    display_input()
    info_country()
    barplot_pop()
    barplot_GDP()
    out_gen()
    login_flask()
    logout_flask()
    page_selection_logout()
    goto_home_page()
