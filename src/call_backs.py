# from dash.dependencies import Input, Output
# from app import app

# from about_page import about_page
# from dash.exceptions import PreventUpdate

# from dash import dcc, html


# # Sample callback using the generated DataTable
# def update_output_div():
#     @app.callback(
#         Output("data_table", "page_size"),
#         [Input("page-size-dropdown", "value")],
#     )
#     def update_page_size(page_size):
#         if page_size is None:
#             raise PreventUpdate
#         return page_size


# # # Callback to update the page content based on the URL
# def page_Selection():
#     @app.callback(Output("page-content", "children"), [Input("url", "pathname")])
#     def display_page(pathname):
#         if pathname == "/page-1":
#             return about_page()
#         elif pathname == "/page-2":
#             return html.Div(
#                 [html.H3("Input field"), html.P("This is content for Page 2.")]
#             )
#         elif pathname == "/page-3":
#             return html.Div(
#                 [html.H3("Simulation"), html.P("This is content for Page 3.")]
#             )
#         else:
#             return html.Div(
#                 [
#                     html.H3("404 - Page not found"),
#                     html.P("The requested URL was not found on the server."),
#                 ]
#             )


# # Registering all callbacks
# def register_callbacks(app):
#     page_Selection()
#     update_output_div()
