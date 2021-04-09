def my_func(a, b, c):
    num = [a, b, c]
    num.remove(min(a, b, c))
    return sum(num)


print(my_func(5, 6, 1))
