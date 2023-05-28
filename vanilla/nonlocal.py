def outside(x):
    free_var = x

    def inside(*arg):
        nonlocal free_var  # solution

        # free var: not declared inside that block
        free_var += y  # UnboundLocalError: cannot modify free variable value
        return free_var
    return inside


concatenate = outside('a')
print(concatenate('b'))
print(concatenate('c'))
print(concatenate('d'))
