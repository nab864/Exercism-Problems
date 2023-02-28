#Given a phrase, count the occurrences of each word in that phrase.

# For the purposes of this exercise you can expect that a word will always be one of:
#
#     A number composed of one or more ASCII digits (ie "0" or "1234") OR
#     A simple word composed of one or more ASCII letters (ie "a" or "they") OR
#     A contraction of two simple words joined by a single apostrophe (ie "it's" or "they're")
#
# When counting words you can assume the following rules:
#
#     The count is case insensitive (ie "You", "you", and "YOU" are 3 uses of the same word)
#     The count is unordered; the tests will ignore how words and counts are ordered
#     Other than the apostrophe in a contraction all forms of punctuation are regarded as spaces
#     The words can be separated by any form of whitespace (ie "\t", "\n", " ")

import re
from collections import Counter

#My Solution
class Wordcount():
    def __init__(self, string1):
        self.string1 = string1
        self.dict = {}

    def count(self):
        self.string1 = self.string1.lower()
        split_string = re.split("\"|:| |!|\n|,|\." , self.string1)
        split_string = [word for word in split_string if word != '']
        split_string = [word.strip("'") for word in split_string]

        for word in split_string:
            if word not in self.dict.keys():
                self.dict[word] = 1
            else:
                self.dict[word] += 1

        return print(self.dict)
test = Wordcount("\"That's the password: 'PASSWORD 123'!\", cried the Special Agent.\nSo I fled.")
print(test.count())
#Exercism Community

def count_words(sentence):
    return Counter(re.findall(r"[a-z0-9]+(?:'[a-z]+)?", sentence.lower()))

print(count_words("\"That's the password: 'PASSWORD 123'!\", cried: the: Special Agent.\nSo I fled."))


