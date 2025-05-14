from flask import Flask
from markupsafe import escape

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "<h1>Welcome to My Flask App!</h1>"

# Static route
@app.route("/about")
def about():
    return "<p>This is a demo Flask app with routing and escaping.</p>"

# Dynamic route with HTML escaping
@app.route("/hello/<name>")
def hello(name):
    return f"<h2>Hello, {escape(name)}!</h2>"

if __name__ == "__main__":
    app.run(debug=True)
