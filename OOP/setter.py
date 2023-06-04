class Pen():
    def __init__(self, color=None):
        self.color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color


blue_pen = Pen()
blue_pen.color = "blue"
print(blue_pen.color)
