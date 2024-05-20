import math

def number_of_cans(height, width, coverage):
   num_of_cans = (height * width) / coverage
   round_cans = math.ceil(num_of_cans)
   print(f"You'll need {round_cans} cans of paint")

height = int(input("Which is the height of the wall?: "))
width = int(input("Which is the width of the wall?: "))
coverage = 5

number_of_cans(height=height, width=width, coverage= coverage)


