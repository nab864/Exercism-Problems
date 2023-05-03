import unittest
from Problems.Bowling import *

class TestFrame(unittest.TestCase):

    def test_add_to_frame(self):
        test = Frame(1)
        test.add_to_frame(4)
        self.assertEqual(test.throws, [4])

    def test_is_strike(self):
        test = Frame(1)
        test.add_to_frame(10)
        self.assertEqual(test.is_strike(), True)
        self.assertEqual(test.is_done, True)

        test = Frame(9)
        test.add_to_frame(10)
        self.assertEqual(test.is_strike(), True)
        self.assertEqual(test.is_done, False)

    def test_is_spare(self):

        test = Frame(1)
        test.add_to_frame(5)
        test.add_to_frame(5)
        self.assertEqual(test.is_spare(), True)
        self.assertEqual(test.is_done, True)

        test = Frame(9)
        test.add_to_frame(10)
        self.assertEqual(test.is_spare(), True)
        self.assertEqual(test.is_done, False)

    def test_frame_score(self):
        '''
        strike
        '''
        test = Bowling()
        test.throw_ball(10)

class TestBowling(unittest.TestCase):

    def test_next_frame(self):
        test = Bowling()
        test.next_frame()
        self.assertEqual(test.current_frame, 1)

    def test_scoring(self):
        test = Bowling()
        test.throw_ball(10)
        test.throw_ball(5)
        test.throw_ball(4)
        test.throw_ball(7)
        self.assertEqual(test.get_total(), 35)

if __name__ == '__main__':
    unittest.main()