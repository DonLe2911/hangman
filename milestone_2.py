#Creating variables for the game

import random

word_list = ["kiwi", "apple", "durian", "dragonfruit", "pear"]

random_word_from_list = random.choice(word_list)

player_guess = input("guess a letter ")

if len(guess) == 1 and player_guess.isalpha():
    print("Valid guess")
else:
    print("Ooops! That is not a valid guess")