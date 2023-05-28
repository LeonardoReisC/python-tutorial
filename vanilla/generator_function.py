def generator(n=0, max=10):
    while True:
        yield n  # pause

        # execute the rest in the next next() call
        n += 1
        if n > max:
            return


gen = generator()
for n in gen:
    print(n)
