import unittest
from collections import Counter


class TestDiscounts(unittest.TestCase):

    def test_discounts(self):
        self.assertEqual(bookstore_discounts([1, 1, 2, 2, 3, 3, 4, 5]), 51.20)
        self.assertEqual(bookstore_discounts([1, 1, 2, 2, 3, 3, 4, 5, 5]), 55.6)
        self.assertEqual(bookstore_discounts([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5]), 102.4)


if __name__ == '__main__':
    unittest.main()


def bookstore_discounts(book_list):
    cnt = Counter(book_list)  # returns a dictionary of the numbers in book_list as keys and how many duplicates as values
    max_duplicate = max(cnt.values())  # returns the max amount of duplicates to help determine how many lists are needed

    split_duplicates = [[] for _ in range(max_duplicate)]  # creates and empty list of lists
    #  for loop to split duplicates into new lists ex. [[1,2,3], [1,2], [1]]
    for book in book_list:
        for i in range(max_duplicate):
            if book not in split_duplicates[i]:
                split_duplicates[i].append(book)
                break
    split_duplicates_len = [len(l) for l in split_duplicates]  # returns a list of the len() of each list in split_duplicates

    # having two groups of 4 is better than a 5 and a 3. adjusts the book grouping into groups of 4 if possible.
    # there might be multiple groups of 5 and 3 so a while loop was used to grab every instance.
    while True:
        if 5 in split_duplicates_len and 3 in split_duplicates_len:
            split_duplicates[split_duplicates_len.index(3)].append(
                split_duplicates[split_duplicates_len.index(5)].pop(-1))
            split_duplicates_len = [len(l) for l in split_duplicates]
        else:
            break

    final_price = 0
    discount_dict = {
        1: 0,
        2: 0.05,
        3: 0.1,
        4: 0.2,
        5: 0.25
    }
    #  determines the final price of the books after discount
    for book_group in split_duplicates:
        final_price += len(book_group) * 8 * (1 - discount_dict[len(book_group)])

    return final_price
