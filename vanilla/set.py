""" SETS
    * mutable data that comprise immutable data
    * dont accept duplicated items
    * data is not indexed 
    * there is no guarantee of sorted elements
    * are iterables(for, in, not in)
"""

set_ = set((1, 2, 3))  # {} -> empty dict/

# METHODS
set_.add('Leo')
print(set_)

set_.update('R')  # update set_ with set('R')
print(set_)

set_.discard('R')  # remove passed value from set_
print(set_)

set_.clear()

# USEFUL OPERATIONS
set1 = {1, 2, 3}
set2 = {2, 3, 4}

print('\n', set1 | set2, sep='')  # same as set1.union(set2)
print(set1 & set2)  # same as set1.intersection(set2)
print(set1 - set2)  # same as set1.difference(set2)

# same as set1.symmetric_difference(set2) -> returns the items that are not in both sets
print(set1 ^ set2)
