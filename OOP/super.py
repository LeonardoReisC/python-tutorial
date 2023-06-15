class A:
    a = 'a'

    def __init__(self, attr):
        self.attr_a = attr

    def method(self):
        print('A')


class B(A):
    b = 'b'

    def __init__(self, attr_a, attr):
        super().__init__(attr_a)  # necessary to avoid losing "attr_a" variable
        self.attr_b = attr

    def method(self):  # overriding
        print('B')


class C(B):
    c = 'c'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("Created object C")

    def method(self):  # overriding
        # calls "method" by accessing it from the class extended by the argument
        super(C, self).method()  # same as super()
        super(B, self).method()
        print('c')


c = C("Leonardo", "Vânia")
print(c.a, c.b, c.c)
c.method()
print(c.attr_a, c.attr_b)
