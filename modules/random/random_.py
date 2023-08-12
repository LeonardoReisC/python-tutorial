# not recommended for sensitive data
import random

# range generators
r_range = random.randrange(10, 20, 2)  # gives a step
print(r_range)

r_range = random.randint(10, 20)  # inclusive stop
print(r_range)

r_uniform = random.uniform(10, 20)  # float numbers inside range
print(r_uniform)
print()

# shuffle
names = ['l', 'e', 'o', 'n', 'a', 'r', 'd', 'o']

random.shuffle(names)  # updates original data
print(names)

# sampling
sample = random.sample(names, k=2)
print(sample)

sample = random.choices(names, k=3)  # allows repetitions
print(sample)

sample = random.choice(names)  # choose a single value
print(sample)
