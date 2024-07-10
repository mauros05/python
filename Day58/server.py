from flask import Flask, render_template
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired()])
    password = PasswordField(label='password', validators=[DataRequired()])

app = Flask(__name__)
app.secret_key = "something-i-dont-know"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
   login_form = LoginForm()
   return render_template("login.html", form=login_form)


if __name__ == "__main__":
    app.run(debug=True)