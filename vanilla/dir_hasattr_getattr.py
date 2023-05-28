string = "leo"
method = 'upper'

print(*dir(string), '', sep='\n')  # returns the attribute names of an object

if hasattr(string, method):  # checks the existence of the method
    print(method, "exists")
    print('output:', getattr(string, method)())  # returns the method
else:
    print(method, 'does not exists')