my_list = []
lenght = int(input('Введите длину списка: '))
for i in range(0, lenght):
    my_list.append(input('Введите список: '))
k = 0
for i in range(len(my_list) // 2):
    my_list[k], my_list[k + 1] = my_list[k + 1], my_list[k]
    k += 2
print(my_list)
