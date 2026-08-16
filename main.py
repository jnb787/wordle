import sys
import requests
import random
from collections import Counter

GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"

try:
    source = requests.get("https://gist.githubusercontent.com/daemondevin/df09befaf533c380743bc2c378863f0c/raw", timeout = 10)
except requests.RequestException as e:
    print(f"Error: Failed to fetch word list - {e}")
    sys.exit()

if source.status_code != 200:
    print(f"Error: Failed to fetch word list - {source.status_code}")
    sys.exit()

word_list = source.text.splitlines()

word = random.choice(word_list).upper()
print(word)
class Wordle:
    def __init__(self):
        self.word = list(word)
        self.word_list = word_list
        self.guesses = 0
        self.saved_boards = []
        self.empty_board = ["_", "_", "_", "_", "_"]

    def guess(self, guess_word):
        guess_word_lowercase = guess_word.lower()
        guess_word_capitalized = guess_word.upper()
        guess = list(guess_word_capitalized)

        if guess_word_lowercase not in self.word_list:
            print("Invalid guess")
            return False

        row = [None] * len(guess)
        remaining = Counter()

        # Pass 1: mark exact matches, and count the answer letters they leave behind.
        for letter in range(len(guess)):
            if guess[letter] == self.word[letter]:
                row[letter] = GREEN + guess[letter] + RESET
            else:
                remaining[self.word[letter]] += 1

        # Pass 2: hand out yellows only while unmatched copies of that letter remain.
        for letter in range(len(guess)):
            if row[letter] is not None:
                continue
            if remaining[guess[letter]] > 0:
                row[letter] = YELLOW + guess[letter] + RESET
                remaining[guess[letter]] -= 1
            else:
                row[letter] = guess[letter]

        self.saved_boards.extend(row)
        self.guesses += 1
        return guess == self.word

    def print_board(self):
        print("Game Board:")
        for round in range(1, self.guesses + 1):
            print(f"Guess {round}:")
            print(" ".join(self.saved_boards[(round - 1) * 5:(round - 1) * 5 + 5]))

        i = 0
        while i < 6 - self.guesses:
            print(" ".join(self.empty_board))
            i += 1

    def run (self):
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
wordle.run()