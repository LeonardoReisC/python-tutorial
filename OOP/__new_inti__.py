# __new__ creates an returns an object based on the 'cls' passed
# __init__ inicialize an instance and returns None
class A:
    def __new__(cls, *args, **kwargs):
        print('__new__')
        instance = super().__new__(cls)
        instance.x = 10
        return instance

    def __init__(self, x):
        self.x = x
        print("__init__")

    def __repr__(self):
        return 'A()'


# a = object.__new__(A)
# a.__init__()
a = A(0)
print(a.x)
