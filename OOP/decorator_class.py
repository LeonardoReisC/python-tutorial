class Multiply:
    def __init__(self, multiplier) -> None:
        self._multiplier = multiplier

    def __call__(self, func):
        def inner(*args, **kwargs): 
            result = func(*args, **kwargs)
            return result*self._multiplier
        return inner
    
@Multiply(6)
def sum(x, y):
    return x+y

sum_ = sum(2, 2)
print(sum_)