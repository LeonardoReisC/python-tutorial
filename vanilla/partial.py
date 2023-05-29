from functools import partial
# partial: implements closure concept

def greet(name, greeting):
    return f'{greeting}, {name}!'

good_morning = partial(greet, greeting='Good morning')
print(good_morning("Leonardo"))