from flask import Flask
import random

rand_number  = random.randint(0,9)
print(rand_number)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='random number' width='500' height='600'>"

@app.route("/<int:user_number>")
def random_number(user_number):
    if user_number > rand_number:
        return "<h1 style='color: purple'>Too high, try again</h1>"\
               "<img src='https://pa1.aminoapps.com/6335/5e3dab49b4d3e708b424887339eb6003a612bead_hq.gif'/>"
    elif user_number < rand_number:
        return "<h1 style='color: red'>Too low, try again</h1>"\
               "<img src='https://pa1.aminoapps.com/6785/c84dc902b2241f1686127a6b2e3b55dc976942a5_00.gif'/>"
    else: 
        return "<h1 style='color: green'>Ya ha ha, you found me</h1>"\
               "<img src='https://media.tenor.com/XFRK9f9fNIkAAAAM/korok-vanish.gif'/>"

if __name__ == "__main__":
    app.run(debug=True)