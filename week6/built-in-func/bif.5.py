def tup_true(tuuple):
    return all(tuuple)

n = input()
tuuple = tuple(eval(n))
print(tup_true(tuuple))