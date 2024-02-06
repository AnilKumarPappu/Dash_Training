# Import Flask and Flask-Login
from flask import Flask, redirect, render_template, request, url_for, make_response


# Create Flask app
server = Flask(__name__)
server.config["SECRET_KEY"] = "your_secret_key"  # Replace with your secret key

# Initialize Flask-Login
# login_manager = LoginManager(server)


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
            response = make_response("good", 200)
            # response.status_code = 200
            return response
    print("into flask")
    return render_template("login.html")


if __name__ == "__main__":
    server.run(debug=True)
    print("Flask is running")
