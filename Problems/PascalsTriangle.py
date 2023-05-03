import unittest


# UnitTest to verify the Rational Class is working properly
class TestStringMethods(unittest.TestCase):

    def test_problem(self):
        self.assertEqual(pascal_row_sum(4), 15)
        self.assertEqual(pascal_row_sum(5), 31)


if __name__ == '__main__':
    unittest.main()


def pascal_row_sum(row):
    if row == 0:
        return 0
    else:
        return 2 ** (row - 1) + pascal_row_sum(row - 1)


print(pascal_row_sum(5))


# string append the previous row onto the new one
def pascal_triangle(row):
    if row == 0:
        return []
    if row == 1:
        return [[1]]
    previous = pascal_triangle(row - 1)
    return previous + [[1] + [a + b for a, b in zip(previous[-1][:-1], previous[-1][1:])] + [1]]


print(pascal_triangle(4))

test = [[1, 3, 3, 1]]
print(test[-1][:-1])
print(test[-1][1:])