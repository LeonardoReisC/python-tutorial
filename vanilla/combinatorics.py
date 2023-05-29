from itertools import combinations, permutations, product


def print_iter(iterator):
    print(*list(iterator), sep='\n', end='\n\n')


people = [
    "Leonardo", "Fernando", "Vânia", "Pedro"
]

t_shirts = [
    ['white', 'black'],
    ['S', 'M', 'L'],
    ['male', 'female', 'unisex']
]

print_iter(combinations(people, 2))
print_iter(permutations(people, 2))
print_iter(product(*t_shirts))
