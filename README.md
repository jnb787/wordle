# wordle

A Python clone of Wordle that runs in the command line, with colored feedback after every guess.

## Requirements

- Python 3.6 or newer
- The [`requests`](https://pypi.org/project/requests/) library
- An internet connection — the word list is downloaded when the game starts

## How to run

From the project root:

```bash
pip install requests
python main.py
```

## How to play

You get **6 guesses** to find a hidden **5-letter word**. After each guess the game reprints the whole board so you can see your history:

```
Game Board:
Guess 1:
S L A T E
Guess 2:
C R A N E
_ _ _ _ _
_ _ _ _ _
_ _ _ _ _
_ _ _ _ _
```

Each letter is colored to tell you how close you were:

| Color | Meaning |
| --- | --- |
| Green | Right letter, right position |
| Yellow | Right letter, wrong position |
| No color | The letter isn't in the word |

Guesses must be real words from the game's word list. Anything else — a made-up word, or the wrong number of letters — is rejected with `Invalid guess` and doesn't cost you a turn.

Repeated letters follow the same rule as real Wordle: a letter is only highlighted as many times as it actually appears in the answer. If the answer has one `E` and you guess a word with three, only one of them lights up — greens claim their letter first, then yellows fill in from whatever is left.

The game ends when you guess the word or use all 6 guesses. If you run out, it reveals the answer.

## Credits

- [Daemondevin](https://github.com/daemondevin) for the word list
