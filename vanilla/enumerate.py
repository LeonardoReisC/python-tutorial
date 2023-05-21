# enumerate: enumerates iterables

names = ["Leonardo", "Fernando", "Vânia"]

enumerated_names = enumerate(names) # returns an iterator
print(enumerated_names, "\n")

for item in enumerated_names:
    print(item, end=" ")
else:
    print("\n")
# iterator points to the end of the list after the for..in loop

for index, value in enumerate(names): # good practice
    print(index, value, sep=" - ")