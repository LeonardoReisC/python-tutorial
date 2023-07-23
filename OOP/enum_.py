# enum: a group of predefined constant names/values
# member: Class[index], Class["key"]
# key: Class.key.name
# value: Class.key.value

import enum

# Directions = enum.Enum("Directions", ['LEFT', 'RIGHT'])
class Direction(enum.Enum):
    LEFT = 1
    RIGHT = 2

# printing enums
print(Direction(1), Direction["LEFT"], Direction.LEFT)
print(Direction(1).name, Direction.LEFT.value, end="\n\n")

def move(direction: Direction):
    if not isinstance(direction, Direction):
        raise ValueError("Direction not found!")

    print(f"Moving to {direction.name}")


move(Direction.LEFT)
move(Direction.RIGHT)
