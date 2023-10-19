import random

word_list = ["kiwi", "apple", "durian", "dragonfruit", "pear"]#

word = random.choice(word_list)

guess = input("guess a letter ")

if len(guess) == 1 and guess.isalpha():
    print("Valid guess")
else:
    print("Ooops! That is not a valid guess")