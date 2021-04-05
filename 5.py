rating = [8, 8, 7, 6]
print('Введите значение,для выхода нажмите q ')
while True:
    mr = (input('Введите значение: '))
    if mr == 'q':
        break
    else:
        rating.append(int(mr))
rating.sort()
rating.reverse()
print(rating)
