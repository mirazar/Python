from functools import reduce
my_list = [i for i in range(100, 1001) if i % 2 == 0]
print(my_list)
number = reduce(lambda a, b: a * b, my_list)
print(number)
