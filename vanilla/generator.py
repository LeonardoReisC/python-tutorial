# Generator: a function that pauses itself
# does not storage an entire data sctructure at once
# generators are not indexed

import sys
from types import GeneratorType

list_ = [n for n in range(1000)]  # already in memory

# not in memory, but it can be acessed one by one
generator = (n for n in range(1000))
print(generator, GeneratorType)

print(sys.getsizeof(list_))  # bytes
print(sys.getsizeof(generator))

# note: elements are printed one by one
for n in generator: # next(generator) function called each loop
    print(n)