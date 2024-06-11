from flask import Flask
import random

app = Flask(__name__)
print(random.__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def say_bye():
    return "<h1>Bye my friend</h1>"

@app.route("/username/<name>")
def greet(name):
    return f"Hello there {name}"


if __name__ == "__main__":
    app.run(debug=True)