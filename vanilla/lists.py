list_a = [1, 2, 3, 4]
list_b = list_a # =(mutable data): points to the same object
list_c = list_a.copy() # creates a copy of list_a

list_b[2] = "Leo" # list_a[2] changed

print(list_a)
print(list_c) # unchanged