from typing import TypeVar

T = TypeVar('T')


def get_item(list: list[T], index: int) -> T:
    return list[index]


list_int = get_item([1, 2, 30], 1)  # -> int
list_str = get_item(['L', 'e', 'o'], 0)  # -> str
