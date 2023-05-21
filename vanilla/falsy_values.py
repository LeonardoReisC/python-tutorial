falsy = [0, 0.0, "", [], (), False, None] # falsy values

print(list(map(lambda x : bool(x), falsy)))

print(True and 0 and False) # and: returns the first falsy value
print(True and 1 and "a") # and: returns the last truly value


print(False or 1 or False) # or: returns the first truly value
print(False or "" or 0.0) # or: returns the last falsy value