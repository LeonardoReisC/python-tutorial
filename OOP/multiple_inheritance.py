# a class can inherit many other classes


# DIAMOND INHERITANCE PROBLEM
#       A
#     /   \
#    B     C
#     \   /
#       D
# Class.mro() | __mro__: shows the mro(Method Resolution Order) of the class
class A:
    ...

    def who_am_i(self):
        print('A')


class B(A):
    ...

    def who_am_i(self):
        print('B')


class C(A):
    ...

    def who_am_i(self):
        print('C')


class D(B, C):  # inheritance order matters - (B,C) != (C,B)
    ...


d = D()
d.who_am_i()

print(D.mro())  # same as D.__mro__
