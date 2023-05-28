# decorator: function that memorizes other functions
# uses the concept of closure

def create_function(func):
    print('Executed before the interpretation start')

    def inner(*args, **kwargs):
        for arg in args:
            is_string(arg)
        result = func(*args, **kwargs)
        return result
    return inner


@create_function  # decorator: runs create_fuction(invert_string)
def invert_string(string):
    print(invert_string.__name__, '\n')  # invert_string --> inner
    return string[::-1]

# encapsulates that error handling form invert_string
def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Parameter must be a string')


# checked_invert_string = create_function(invert_string)
# print(checked_invert_string('Leonardo'))
print(invert_string("Leonardo"))
