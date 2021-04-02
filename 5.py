proceeds = int(input('Введите выручку: '))
costs = int(input('Введите расход: '))
profit = proceeds - costs
if profit < 0:
    print('Работаем в убыток')
elif profit == 0:
    print('Прибыли нет')
else:
    print(f'Имеется прибыль {profit}')
    print(f'Рентабельность {(profit / proceeds) * 100:1.2f}%')
    stuff = int(input('Введите количество сотрудников: '))
    print(f'Прибыль на сотрудника {profit / stuff:1.2f}')
