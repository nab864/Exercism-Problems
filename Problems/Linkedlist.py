
class Node:
    def __init__(self, station, before=None, after=None):
        self.station = station
        self.before = before
        self.after = after

    def __str__(self):
        return f"Node({self.station},{self.before}, {self.after})"

    def __eq__(self, other):
        return self.station == other.station

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.empty = True
        self.single = False

    def __len__(self):
        count = 0
        node = self.first
        while node:
            node = node.after
            count += 1
        return count

    def push(self, value):
        node = Node(value)
        if self.empty:
            self.first = node
            self.last = node
            self.empty = False
            self.single = True
        elif self.single:
            node.before = self.first
            self.first.after = node
            self.last = node
            self.single = False
        else:
            node.before = self.last
            self.last.after = node
            self.last = node

    def unshift(self, value):
        node = Node(value)
        if self.empty:
            self.first = node
            self.last = node
            self.empty = False
            self.single = True
        elif self.single:
            node.after = self.first
            self.first.before = node
            self.first = node
            self.single = False
        else:
            node.after = self.first
            self.first.before = node
            self.first = node

    def pop(self):
        if self.empty:
            raise ValueError('List is empty')
        else:
            self.last = self.last.before
            self.last.after = None

    def shift(self):
        if self.empty:
            raise ValueError('List is empty')
        else:
            self.first = self.first.after
            self.first.before = None

    def delete(self, value):
        node = self.first
        found = False
        while node:
            if node == Node(value):
                node.before.after = node.after
                node.after.before = node.before
                found = True
                break
            node = node.after
        if not found:
            raise ValueError("Value not found")