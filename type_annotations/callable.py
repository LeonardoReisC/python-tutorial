from collections.abc import Callable

sum_integers = Callable[[int, int], int]  # Callable[[parameters], return]


def exec(func: sum_integers, a: int, b: int) -> int:
    return func(a, b)


def sum_(a: int, b: int) -> int:
    return a + b


print(exec(sum_, 1, 2))
