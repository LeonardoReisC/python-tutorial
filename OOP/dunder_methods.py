class Point:
    def __init__(self, x, y, z="String"):
        self.x = x
        self.y = y
        self.z = z

    # call the string representation of an object
    def __str__(self):
        return f'({self.x}, {self.y})'

    # representation of the object(for devs)
    def __repr__(self):
        # must be entirely repr'ed
        return f'{self.__class__.__name__}(x= {self.x!r}, y={self.y!r}, z={self.z!r})'

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point(new_x, new_y)

    def __gt__(self, other):
        euclidean_self = (self.x**2 + self.y**2)**0.5
        euclidean_other = (other.x**2 + other.y**2)**0.5
        return euclidean_self > euclidean_other


p1 = Point(-2, -4)
p2 = Point(1, 2)
print(f'{p1!s}')  # same as p1
print(f'{p2!r}', '\n')  # same as repr(p2)

p3 = p1 + p2
print(p3, '\n')

print("P1 is greater than P2:", p1 > p2)
print("P2 is greater than P1:", p2 > p1)
