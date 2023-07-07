# using decorators with methods

def my_planet(method):
    def inner(self, *args, **kwargs):
        result = method(self, *args, **kwargs)

        if "Earth" in result:
            return "You are at home"
        return result
    return inner


class Team:
    def __init__(self, name) -> None:
        self.name = name


class Planet:
    def __init__(self, name) -> None:
        self.name = name

    @my_planet
    def say_name(self):
        return f"Your planet is {self.name}"


brazil = Team("Brazil")
france = Team("France")

earth = Planet("Earth")
saturn = Planet("Saturn")

print(earth.say_name())
print(saturn.say_name())
