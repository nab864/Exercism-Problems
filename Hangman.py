import unittest

class TestStringMethods(unittest.TestCase):

    def test_gameboard(self):
        self.assertEqual(Hangman('yelp', 5).game_board, ['_', '_', '_', '_'])

if __name__ == '__main__':
    unittest.main()


class Hangman:
    def __init__(self, word, num_guesses):
        self.indices = None
        self.guess = None
        self.word = word
        self.num_guesses = num_guesses
        self.game_status = True
        self.game_board = ['_' for i in range(len(word))]

    def __repr__(self):
        return print(self.game_board, f'You have {self.num_guesses} guesses left.')


    def get_status(self):
        if '_' not in self.game_board:
            self.num_guesses = 0
            return print(self.game_board, "You won the game!")
        if self.num_guesses == 0:
            if '_' in self.game_board:
                return print(self.game_board, "You lost the game!")
            return print(self.game_board, "You won the game!")
        return print(self.game_board, f'You have {self.num_guesses} guesses left.')

    def make_guess(self, guess):
        if self.num_guesses == 0:
            raise ValueError("The game has already ended.")
        self.guess = guess
        if len(self.guess) != len(self.word) and len(self.guess) != 1:
            raise ValueError('Guess must be a single letter or the same character length as the word.')
        self.num_guesses -= 1

        if len(self.guess) == len(self.word):
            if self.guess == self.word:
                for i in range(len(self.guess)):
                    self.game_board[i] = self.guess[i]
                return self.get_status()
            return self.get_status()

        self.indices = []

        for num in range(len(self.word)):
            if self.word[num] == self.guess:
                self.indices.append(num)

        if len(self.indices) == 0:
            return self.get_status()

        for i in self.indices:
            self.game_board[i] = self.guess
        return self.get_status()


test = Hangman('yelp', 5)
test.__repr__()
test.make_guess('yelp')