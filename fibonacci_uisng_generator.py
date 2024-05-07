# fibonacci sequency is 0, 1, 1, 2, 3, 5, 8, 13 ....

# Here we produce fibonacci sequences using generator

def fib():
    a = 0
    b = 1

    while True:
        yield a
        a, b = b, a + b

for f in fib():
    if f > 50:
        break
    print(f)
