# pylint: disable=too-few-public-methods
"""Game module for word validation based on a randomized grid."""

import random
import string
import nltk

# Ensure the English words corpus is available
nltk.download('words')
from nltk.corpus import words

class Game:
    """A class representing a word validation game."""

    def __init__(self):
        """Initialize a random grid of size 9."""
        self.grid = ''.join(random.choices(string.ascii_uppercase, k=9))

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word can be formed using the Game's grid and is in the dictionary."""
        if not word:
            return False

        grid_letters = list(self.grid)

        for letter in word:
            if letter in grid_letters:
                grid_letters.remove(letter)  # Remove used letter to avoid reuse
            else:
                return False

        return word.lower() in words.words()

if __name__ == "__main__":
    game = Game()
    print("Grid:", game.grid)

    WORD_TO_CHECK = "BAROQUE"
    print(f"Is '{WORD_TO_CHECK}' valid?:", game.is_valid(WORD_TO_CHECK))
