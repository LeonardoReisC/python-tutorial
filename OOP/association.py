# Gererally, an association happens when a object reference another one
# There is no specification about lifecycle control from one object to another
class Writer:
    def __init__(self, name):
        self.name = name
        self.tool = None

    @property
    def tool(self):
        return self._tool

    @tool.setter
    def tool(self, ferramenta):
        self._tool = ferramenta


class WritingTool:
    def __init__(self, name):
        self.name = name

    def write(self):
        return f'{self.name} is writing...'


writer = Writer("Leonardo")
pen = WritingTool("Faber Castell")
writer.tool = pen

print(writer.tool.write())
