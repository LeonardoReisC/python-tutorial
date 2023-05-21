names = ["Leonardo", "Fernando", "João"]

name1, name2, name3 = names # general unpacking

name1, *rest = names # unpacks the desired value
print(name1, rest)

_, name2, *_ = names # good practice: use "_" variable name to show that "_" will not be used

print(name2, _)