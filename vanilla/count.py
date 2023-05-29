from itertools import count

# count: an endless iterator
it = count(3, 3)

print(hasattr(it, "__iter__")) # is an iterable
print(hasattr(it, "__next__")) # is an iterator

for i in it:
    if i >= 10:
        break
    print(i)