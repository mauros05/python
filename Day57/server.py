from flask import Flask, render_template
import random
import datetime
import requests

app =  Flask(__name__)

@app.route("/")
def hello_world():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.today().year
    return render_template("index.html", num = random_number, year = current_year)

@app.route("/guess/<name>")
def guess(name):
    gender_url = f"https://api.genderize.io/?name={name}"
    gender_response =  requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]

    age_url = f"https://api.agify.io/?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("guess.html", personal_name = name, gender = gender, age = age)

@app.route("/blog")
def get_blog():
    current_year = datetime.datetime.today().year
    posts_url = "https://api.npoint.io/e89ec700ad8552c04598/"
    posts_request = requests.get(posts_url)
    posts_data = posts_request.json()
    return render_template("blog.html", posts = posts_data, year = current_year)

@app.route("/blog/<int:id>")
def show_post(id):
    current_year = datetime.datetime.today().year
    new_id = id - 1
    post_url = f"https://api.npoint.io/e89ec700ad8552c04598/{new_id}"
    post_request = requests.get(post_url)
    post_data = post_request.json()
    return render_template("show.html", post = post_data, year = current_year)

if __name__ == "__main__":
    app.run(debug=True)