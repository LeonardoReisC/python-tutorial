
def addition(*args):    # unpacks an unnamed-argumented iterable
    return sum(*args)


numbers = 1, 2, 3, 4, 5, 6

print(addition([1, 2, 3]))
print(addition(numbers))
