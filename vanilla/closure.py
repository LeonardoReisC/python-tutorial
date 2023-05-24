
def greeting(greeting):
    def to_greet(name):
        print(f"{greeting}, {name}!")
    return to_greet # greeting parameter gets stored for further calls

good_morning = greeting("Good morning")
good_night = greeting("Good night")

good_morning("Leo")
good_night("Leo")