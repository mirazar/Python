class OwnError(Exception):
    pass


def div():
    try:
        num1 = int(input('Введите делимое: '))
        num2 = int(input('Введите делитель: '))
        if num2 == 0:
            raise OwnError("Делить на ноль нельзя!")
        else:
            res = num1 / num2
            return res
    except ValueError:
        return "Вы ввели не число"
    except OwnError as err:
        return err


print(div())
