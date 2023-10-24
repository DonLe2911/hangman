#putting everything together

import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.num_lives = num_lives
        self.guessed_so_far = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_letters_tried = []

#method to check if guessed letter is in word
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in list(self.word):
            self.list_letters_tried.append(guess)
            for i in range(0, len(self.word)):
                if self.word[i] == guess:
                    self.guessed_so_far[i] = guess
                    self.num_letters -= 1
            print(f"Good guess! {guess} is in the word")
            print(self.guessed_so_far)
        else:
            self.list_letters_tried.append(guess)
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word")
            print(f"you have {self.num_lives} number of lives left")

#method asking for player guess, checks that it is a single alphabetocal character and whether it has alread been guessed or not     
    def ask_for_input(self):
        guess = input("Guess a letter ")
        print(f"number of unique letters remaining is {self.num_letters}")
        if guess in self.list_letters_tried:
            print(f"{guess} already tried")
        elif len(guess) != 1 or not guess.isalpha():
            print("Invalid letter, please enter a single alphabetical character")
        else:
            self.check_guess(guess)
            print(f"list of letters already tried {self.list_letters_tried}")

#mehtod to play the game        
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:       
        if game.num_lives == 0:
            print("Game Over")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print({game.word})
            print("Congratulations, you won the game")
            break

#initialising word lsit and an instance of the game
word_list = ["don", "laura", "lann", "vivi", "thuthu", "baba"]
play_game(word_list)
