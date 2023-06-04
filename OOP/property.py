"""
    property: decorator that makes an object methos acts like an attribute
    generally used
        - as a getter
        - to avoid breaking client codes
        - to enable a setter
        - to run some actions when getting an attribute 
"""


class Pen():
    def __init__(self, color):
        self._color = color  # _name: dev pointing to a private/protected variable

    @property
    def color(self):
        return self._color


blue_pen = Pen("blue")
print(blue_pen.color)  # encapsulates _color attribute
