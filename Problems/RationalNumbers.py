import unittest
import math


# UnitTest to verify the Rational Class is working properly
class TestStringMethods(unittest.TestCase):
    def test_added(self):
        self.assertEqual(Rational(4, 6) + Rational(5, 8), Rational(31, 24))

    def test_subtracted(self):
        self.assertEqual(Rational(4, 6) - Rational(5, 8), Rational(1, 24))

    def test_divided(self):
        self.assertEqual(Rational(4, 6) / Rational(5, 8), Rational(16, 15))
        self.assertEqual(Rational(4, 6) / Rational(5, 8), Rational(32, 30))

    def test_multiply(self):
        self.assertEqual(Rational(4, 6) * Rational(5, 8), Rational(5, 12))

    def test_exponential(self):
        self.assertEqual(Rational(4, 6) ** 2, Rational(4, 9))
        self.assertEqual(Rational(4, 6) ** -2, Rational(4, 9))
        self.assertEqual(2 ** Rational(4, 6), 2 ** (4 / 6))

    def test_abs(self):
        self.assertEqual(abs(Rational(-4, -6)), Rational(4, 6))


if __name__ == '__main__':
    unittest.main()


class Rational:
    def __init__(self, numerator, denominator):
        self.gcd = math.gcd(numerator, denominator)  # Determines the Greatest Common Denominator
        self.numerator = int(numerator / self.gcd)  # Reduces the numerator by the GCD
        self.denominator = int(denominator / self.gcd)  # Reduces the numerator by the GCD

    # Returns the numerator and denominator as strings, I.E. '4/6'
    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    # The following functions add mathematical operations to the Rational Object
    def __add__(self, other):
        return Rational(self.numerator * other.denominator + other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __sub__(self, other):
        return Rational(self.numerator * other.denominator - other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __truediv__(self, other):
        return Rational(self.numerator * other.denominator, self.denominator * other.numerator)

    def __mul__(self, other):
        return Rational(self.numerator * other.numerator, self.denominator * other.denominator)

    def __abs__(self):
        return Rational(abs(self.numerator), abs(self.denominator))

    def __pow__(self, power, modulo=None):
        return Rational(self.numerator ** abs(power), self.denominator ** abs(power))

    def __rpow__(self, other):
        return other ** (self.numerator / self.denominator)

    #Allows the comparison between Rational Objects
    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator


four_sixths = Rational(4, 6)
five_eighths = Rational(5, 8)
addition = 2 ** four_sixths
print(addition)
