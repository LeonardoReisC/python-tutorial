# dataclasses are syntax sugar
# https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass, asdict, astuple, field


@dataclass
class Person:
    # default values only accepted for immutable data
    name: str = "Missing"
    surname: str = "Not sent"
    age: int = 1
    addresses: list[str] = field(default_factory=list)  # mutable data way

    # executed right after __init__
    def __post_init__(self):
        self.full_name = f"{self.name} {self.surname}"


if __name__ == "__main__":
    p1 = Person("Leonardo", "Reis")  # __init__
    p2 = Person("Leonardo", "Reis")
    print(p1)  # __repr__
    print(p1 == p2)  # __eq__
    print('')

    print(p1.full_name)
    print('')

    print(asdict(p1))
    print(astuple(p1))
