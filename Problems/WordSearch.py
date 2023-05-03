import unittest
from stringcolor import *
from termcolor import colored, cprint

# class TestStringMethods(unittest.TestCase):
#
#     def test_WordSearch(self):
#         pass
#         # self.assertEqual(Hangman('yelp', 5).game_board, ['_', '_', '_', '_'])
#
# if __name__ == '__main__':
#     unittest.main()


test_string = "jefblpepre\ncamdcimgtc\noivokprjsm\npbwasqroua\nrixilelhrs\nwolcqlirpc\nscreeaumgr\nalxhpburyi\njalaycalmp\nclojurermt"


class Wordsearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.puzzle_list = [line for line in puzzle.split("\n")]

    def find(self, word):
        self.word = word
        self.reverse_word = word[::-1]
        self.first_and_last_coord = None
        self.coordinate_change = [(-len(word), -len(word)), (0, -len(word)), (len(word), -len(word)), (len(word), 0),
                                  (len(word), len(word)), (0, len(word)), (-len(word), len(word)), (-len(word), 0)]
        for i in range(len(self.puzzle_list)):
            if self.puzzle_list[i].find(self.word) != -1:
                first_letter = (i, self.puzzle_list[i].find(self.word))
                last_letter = (i, self.puzzle_list[i].find(self.word) + len(word))
                self.first_and_last_coord = [first_letter, last_letter]
                return self.first_and_last_coord
            elif self.puzzle_list[i].find(self.reverse_word) != -1:
                first_letter = (i, self.puzzle_list[i].find(self.reverse_word))
                last_letter = (i, self.puzzle_list[i].find(self.reverse_word) + len(word))
                self.first_and_last_coord = [first_letter, last_letter]
                return self.first_and_last_coord
        row = 0
        for line in self.puzzle_list:
            column = 0
            for character in line:
                if character == self.word[0]:
                    for coord in self.coordinate_change:
                        try:
                            if self.puzzle_list[row + coord[0]][column + coord[1]] == self.word[-1] and self.puzzle_list[row + coord[0] - 1][column + coord[1] - 1] == self.word[-2]:
                                return [(row, column), (row + coord[0], column + coord[1])]
                        except:
                            pass
                column += 1
            row += 1


test = Wordsearch(test_string)
print(test.find('pile'))

test = 'pile'
print(test[::-1])
