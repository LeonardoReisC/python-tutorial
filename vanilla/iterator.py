name = "Leonardo"

it = iter(name)  # __iter__() also works

print(next(it))  # __next__() also works
print(next(it))
print(next(it))

# returns an StopIteration error exception in the end of an iterable
