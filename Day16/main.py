import another_module

print(another_module.another_variable)

# import turtle
# fredo = turtle.Turtle()

from turtle import Turtle, Screen
fredo = Turtle()
print(fredo)
fredo.color("red", "green")
fredo.shape("turtle")
fredo.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
