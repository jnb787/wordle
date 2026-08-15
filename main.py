import requests
import random

GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"
source = requests.get("https://gist.githubusercontent.com/daemondevin/df09befaf533c380743bc2c378863f0c/raw")

if source.status_code == 200:
    word_list = source.text.splitlines()
else:
    print("Error: Failed to fetch word list")
    exit()

word = word_list[random.randint(0, len(word_list) - 1)].upper()
print(word)
class Wordle:
    def __init__(self):
        self.word = list(word)
        self.guesses = 0
        self.guessed_letters = []
        self.saved_boards = []
        self.empty_board = ["_", "_", "_", "_", "_"]

    def guess(self, guess_word):
        guess_word_lowercase = guess_word.lower()
        guess_word_capitalized = guess_word.upper()
        guess = list(guess_word_capitalized)

        if guess_word_lowercase not in word_list:
            print("Invalid guess")
            return False
        else:
            if list(self.word) == guess:
                self.guesses += 1
                for letter in range(len(guess)):
                    self.saved_boards.append(GREEN + guess[letter] + RESET)
                return True

            else:
                letter = 0
                for letter in range(len(guess)):
                    if guess[letter] == self.word[letter]:
                        self.saved_boards.append(GREEN + guess[letter] + RESET)
                    elif guess[letter] in self.word:
                        self.saved_boards.append(YELLOW + guess[letter] + RESET)
                    else:
                        self.saved_boards.append(guess[letter])
                    letter += 1
                
                self.guesses += 1
                return False

    def print_board(self):
        print("Game Board:")
        round = 1
        for round in range(1, self.guesses + 1):
            print(f"Guess {round}:")
            print(" ".join(self.saved_boards[(round - 1) * 5:(round - 1) * 5 + 5]))

        i = 0
        while i < 6 - self.guesses:
            print(" ".join(self.empty_board))
            i += 1

    def main (self):
        print("Worldle Game")
        self.print_board()
        while True:
            guess = input("Guess a 5-letter word: ")
            if self.guess(guess):
                self.print_board()
                print("You won!")
                break
            elif self.guesses == 6:
                self.print_board()
                print("You lost!")
                print(f"The word was: {''.join(self.word)}")
                break
            else:
                self.print_board()

wordle = Wordle()
wordle.main()