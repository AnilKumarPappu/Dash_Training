# Import Flask and Flask-Login
from flask import Flask, redirect, render_template, request, url_for, make_response
from flask_login import (
    LoginManager,
    login_user,
    current_user,
    login_required,
    logout_user,
)

# from app2 import app

# Create Flask app
server = Flask(__name__)
server.config["SECRET_KEY"] = "your_secret_key"  # Replace with your secret key

# Initialize Flask-Login
login_manager = LoginManager(server)


class User:
    def __init__(self, user_id, username, password):
        self.id = user_id
        self.username = username
        self.password = password

    def is_authenticated(self):
        # Implement your authentication logic here
        return self.username == "admin" and self.password == "password"

    def is_active(self):
        return True

    def get_id(self):
        return str(self.id)


@login_manager.user_loader
def load_user(user_id):
    # Replace this with your actual user loading logic
    return User(user_id)


@server.route("/login", methods=["GET", "POST"])
def login():
    print("into flask")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        print("login called")
        # Replace this with your actual authentication logic
        # Check if the provided credentials are valid
        if username == "admin" and password == "password":
            user = User(1, username, password)
            login_user(user, force=True)
            print(login_user(user))
            # print(redirect(url_for("/page")))
            # response = make_response(redirect(url_for("page")))
            response = make_response("good", 200)
            # response.status_code = 200
            return response
    print("into flask")
    return render_template("login.html")


@server.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))  # Replace 'index' with your home page route


@server.route("/page")
@login_required
def render_dashboard():
    print("rendered")
    return "Welcome to the Dashboard!"


if __name__ == "__main__":
    server.run(debug=True)
    print("Flask is running")
