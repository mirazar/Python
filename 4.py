def my_func(x, y):
    return 1 / x**abs(y)


print(my_func(5, 2))


def my_func_exp(x, y):
    for i in range(abs(y - 1)):
        x *= x
    return 1 / x


print(my_func_exp(5, 2))
