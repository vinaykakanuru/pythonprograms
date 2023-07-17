"""
Concatenate two dictionaries if key exists in two dictionaries add the values
"""

# Example Input:
d1 = {"a":1, "b":2, "d":4}
d2 = {"b":3, "c":3}

# Output:
# res = {"a":1, "b":5, "c":3, "d":4}

from collections import Counter
from operator import add
from functools import reduce

print(dict(reduce(add, (map(Counter, [d1, d2])))))

def add_dicts(d1, d2):
    for key, val in d1.items():
        if key in d2:
            d2[key] = d2[key] + val
        else:
            d2[key] = val
        
    return d2

print(f"merging two dicts using for loop: {add_dicts(d1, d2)}")




