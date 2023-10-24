#Check if guessed character is in the word

import random

word_list = ["kiwi", "apple", "durian", "dragonfruit", "pear"]

random_word_from_list = random.choice(word_list)


def check_guess(guess):
    guess = guess.lower()
    if guess in random_word_from_list:
        print(f"Good guess! {guess} is in the word")
    else:
        print(f"Sorry, {guess} is not in the word")


def ask_for_input():
       
    while True:
        guess = input("Guess a letter ")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter, please enter a single alphabetical character")
    
    check_guess(guess)
    
ask_for_input()