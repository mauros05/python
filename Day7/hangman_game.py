import random
import word_list

word_list = word_list.word_list

random_word = random.choice(word_list)

word_length = len(random_word)

display_word = []

for letter in range(word_length):
    display_word.append("_")

print(display_word)

end_of_game = False
attemps = 6

while end_of_game == False:
    user_input = input("Guess a letter: ").lower()

    if user_input in display_word:
        print(f"You've already guessed {user_input}")

    for position in range(word_length):
        letter = random_word[position]
        if letter == user_input:
            display_word[position] = letter
            print(f"Correct! letter {user_input} is on the word")
  
    print(display_word)

    if user_input not in random_word:
        attemps -= 1
        print(f"You have {attemps} attemps reminded")
        if attemps == 0:
            end_of_game = True
            print("You Lose")


    if "_" not in display_word:
        end_of_game = True
        print("You Win!")
    
