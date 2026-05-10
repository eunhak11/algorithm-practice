"""
Q1 — Duplicates allowed

Implement a data store class with two methods:

insert(val) — add a value (duplicates allowed)
remove() — remove any one element and return it

"""

class DataStore:
    def __init__(self):
        self.data = []

    def insert(self, val):
        self.data.append(val)

    def remove(self):
        if self.data:
            return self.data.pop()
        else:
            raise IndexError("Store is empty")