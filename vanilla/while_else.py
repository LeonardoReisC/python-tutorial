i = 10
odd_counter = 0

while i:
    i -= 1
    if not i % 2:
        odd_counter += 1
else: # executes only if condition is False
    print(f'There are {odd_counter} numbers within [0,10]')
