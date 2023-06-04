"""
    ACCESS MODIFIER CONVENTIONS
    - public variable
        * var (without underscore)
    - protected variable
        * _var (one underscore)
    - private variable
        * __var (two underscores)
        * name mangling: _ClassName__attr_or_method
"""


class Foo:
    def __init__(self):
        self.public = "public attribute"
        self._protected = "protected attribute"
        self.__private = "private attribute"

    def public_method(self):
        return "public method"

    def _protected_method(self):
        return "protected method"

    def __private_method(self):
        return "private method"


f = Foo()
print(f.public)
print(f.public_method())

print(f._protected)
print(f._protected_method())

print(f._Foo__private)  # alerts devs that it is a private attribute
print(f._Foo__private_method())  # alerts devs that it is a private method
