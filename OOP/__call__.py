class CallMe:
    def __init__(self, phone) -> None:
        self.phone = phone

    # make the instance callable
    def __call__(self, name):
        return f"{name} is calling {self.phone}"


call = CallMe("(01) 2345-6789")
print(call("Leonardo"))
