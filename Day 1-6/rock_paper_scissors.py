import random

answer = random.randint(1,3)

print("Let's play Rock, Paper, Scissors")
print("What do you chose?")
print("1-rock 2-paper 3-scissors")

user_answer = int(input(">"))


if answer == user_answer:
    print("Tie, you and the computer chose the same item")
elif answer == 1 and user_answer == 2:
    print("You win, You choose Paper and the Computer chooses Rock")
elif answer == 1 and user_answer == 3:
    print("You Lose, You choose Scissors and the Computer chooses Rock")
elif answer == 2 and user_answer == 1:
    print("You lose, You choose Rock and the Computer chooses Scissors")
elif answer == 2 and user_answer == 3:
    print("You win, You choose Scissors and the Computer chooses Paper")
elif answer == 3 and user_answer == 1:
    print("You win, You choose Rock and the Computer chooses Scissors")
elif answer == 3 and user_answer == 2:
    print("You lose, You choose Paper and the Computer chooses Scissors")
else:
    print("I don't recognize your answer") 



