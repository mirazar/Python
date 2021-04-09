def func_divide():
    try:
        a = float(input('Введите первое число: '))
        b = float(input('Введите второе число: '))
        return a / b
    except ZeroDivisionError:
        return


print(func_divide())
