"""
Q2 — No duplicates

Modify your solution from Q1 so that:

Inserting a duplicate value is silently ignored
remove() still removes and returns any one element
Also explain the time complexity of each method
"""

class DataStore:
    def __init__(self):
        self.data = set()

    def insert(self, val):
        self.data.add(val)

    def remove(self):
        if self.data:
            return self.data.pop()
        else:
            raise IndexError("Store is empty")

"""
time complexity of list is  O(n) >> index based (from head to tail)
time complexity of set is O(1) >> hash based (directly)

답변:
I changed the data structure from a list to a set to improve the time complexity from O(n) to O(1)
"""