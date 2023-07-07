# using decorators with classes to share the same __repr__ method

def add_repr(cls):
    def my_repr(self):
        return f"{self.__class__.__name__}({self.__dict__})"
    cls.__repr__ = my_repr
    return cls

# same as: Team = add_repr(Team)
@add_repr
class Team:
    def __init__(self, name) -> None:
        self.name = name

# same as: Team = add_repr(Team)
@add_repr
class Planet:
    def __init__(self, name) -> None:
        self.name = name


brazil = Team("Brazil")
print(brazil, "\n")

france = Team("France")
print(france, "\n")

earth = Planet("Earth")
print(earth, "\n")

saturn = Planet("Saturn")
print(saturn, "\n")
