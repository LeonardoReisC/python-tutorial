falsy = [0, 0.0, "", False, None] # falsy values

print(list(map(lambda x : bool(x), falsy)))

print(True and 0 and False) # return the first falsy value