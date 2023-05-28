# raise: forces an specified error to occur
# https://docs.python.org/3/library/exceptions.html
def reject_non_numbers(number):
    if not isinstance(number, (int, float)):
        raise TypeError(
            f'"{number}" must be int or float. '
            f'\n\t\t"{type(number).__name__}" sent'
        )

def reject_zero(number):
    if number == 0:
        raise ZeroDivisionError("Zero is not allowed")

def divide(n, d):
    reject_non_numbers(n)
    reject_non_numbers(d)
    reject_zero(d)
    return n/d

print(divide(8, 0))
