"""
Implement a data store class with three methods:

insert(val) — add a value (duplicates allowed)
remove() — remove and return the minimum value
get_min() — return the minimum value without removing it
Example:
insert(3) → insert(1) → insert(2)
get_min() → 1
remove() → 1
get_min() → 2

"""
import sys

class DataStore:
    def __init__(self):
        self.data = []
        self.min = sys.maxsize

    def insert(self, val):
        self.data.append(val)
        self.min = val if val<self.min else self.min

    def remove(self):
        if self.data:
            rm_var = self.min
            self.data.remove(self.min)
            self.min = min(self.data) if self.data else sys.maxsize
            return rm_var
        else:
            raise IndexError("Store is empty")

    def get_min(self):
        if self.data:
            return self.min
        else:
            raise IndexError("Store is empty")

"""
time complexity
insert | O(1) : 가장 뒤에 바로 들어가니까
remove | O(n) : remove(), min()이 O(n)이기 때문에 O(n) 
get_min : O(1)
"""