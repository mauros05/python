import random

names = ["Mauricio", "Julio", "Conchis", "Betty"]

number_of_names = len(names)

random_number = random.randint(0, number_of_names - 1)


print("Who is going to pay the bill?")
print(names[random_number])