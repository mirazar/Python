a = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
b = [i for i, el in zip(a[1:], a[:-1]) if i > el]
print(b)
