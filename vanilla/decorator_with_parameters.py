def create_decorator(name):
    def create_function(func):
        print('Decarator:', name)

        def inner(*args, **kwargs):
            result = func(*args, **kwargs)  # recursive
            final = f'{result} {name}'
            return final
        return inner
    return create_function


@create_decorator(5)
@create_decorator(4)
@create_decorator(3)
@create_decorator(2)
@create_decorator(1)
def sum_(x, y):
    return x+y


print(sum_(10, 5))
