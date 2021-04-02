max_num = 0
while True:
    num = int(input('Введите число: '))
    if num < 0:
        print('Введите положительное число')
    else:
        while num > 0:
            if num > max_num:
                max_num = num % 10
            num = num // 10
        print(max_num)
        break
