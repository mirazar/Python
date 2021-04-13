import itertools


def iter_func(a):
    for el in itertools.count():
        print(el)
        if el == 10:
            break


iter_func(3)


def cycle_func():
    c = 0
    for el in itertools.cycle("ABC"):
        if c > 10:
            break
        print(el)
        c += 1


cycle_func()
