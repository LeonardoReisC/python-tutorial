# https://docs.python.org/3/library/exceptions.html
class MyError(Exception):
    ...


class AnotherError(Exception):
    ...


def raise_():
    exception = MyError("My", "error", "message")
    raise exception


try:
    raise_()
except (MyError, TypeError) as error:
    print(error.__class__.__name__)
    print(error)

    exception = AnotherError("Gonna raise again")
    raise exception from error
