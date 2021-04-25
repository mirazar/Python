num = [i for i in range(1, 21, 2)]
with open('sum.txt', 'w', -1, 'utf-8') as f:
    f.write(" ".join([str(i) for i in range(1, 21, 2)]))
with open('sum.txt') as f:
    print(sum(map(int, f.readline().split())))
