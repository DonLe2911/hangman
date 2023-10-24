#Creating the hangman game class 

import random


class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.num_lives = num_lives
        self.guessed_so_far = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_letters_tried = []

  
    def check_guess(self, guess):
        self.guess = self.guess.lower()
        if guess in list(self.word):
            self.list_letters_tried.append(guess)
            for i in range(0, len(self.word)):
                if self.word[i] == guess:
                    self.guessed_so_far[i] == guess
                    self.num_letters -= 1
            print(f"Good guess! {guess} is in the word")
            print(self.guessed_so_far)
        else:
            self.list_letters_tried.append(guess)
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word")
            print(f"you have {self.num_lives} left")
    
    def ask_for_input():
        while True:
            guess = input("Guess a letter ")
            if guess in self.list_letters_tried:
                print(f"{guess} already tried")
            elif len(guess) == 1 and guess.isalpha():
                print("Invalid letter, please enter a single alphabetical character")
            else:
                self.check_guess(guess)
            
        