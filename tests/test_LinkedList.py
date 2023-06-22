import unittest
from Problems.Linkedlist import *

class TestLinkedList(unittest.TestCase):

    def test_node(self):
        pass

    def test_push(self):
        test = LinkedList()
        test.push(1)
        self.assertEqual(test.first, Node(1))
        self.assertEqual(test.last, Node(1))
        test.push(2)
        self.assertEqual(test.first, Node(1))
        self.assertEqual(test.last, Node(2))
        test.push(3)
        self.assertEqual(test.first, Node(1))
        self.assertEqual(test.last, Node(3))
        test.push(4)
        self.assertEqual(test.last.before, Node(3))


    def test_pop(self):
        test = LinkedList()
        test.push(1)
        test.push(2)
        test.push(3)
        test.pop()
        self.assertEqual(test.last, Node(2))

    def test_shift(self):
        test = LinkedList()
        test.push(1)
        test.push(2)
        test.push(3)
        test.push(4)
        test.shift()
        self.assertEqual(test.first, Node(2))
        test.shift()
        self.assertEqual(test.first, Node(3))

    def test_unshift(self):
        test = LinkedList()
        test.unshift(1)
        test.unshift(2)
        self.assertEqual(test.first, Node(2))
        self.assertEqual(test.last, Node(1))

    def test_len(self):
        test = LinkedList()
        test.push(1)
        test.push(2)
        self.assertEqual(len(test), 2)
        test.push(3)
        self.assertEqual(len(test), 3)
        test.push(4)
        self.assertEqual(len(test), 4)

if __name__ == '__main__':
    unittest.main()