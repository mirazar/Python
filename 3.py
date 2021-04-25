with open('wages.txt', 'r', -1, 'utf-8') as f:
    salary = []
    for line in f:
        text = line.split()
        salary.append(float(text[1]))
        if float(text[1]) < 20000:
            print(line, end='')
average = sum(salary) / len(salary)
print('Средняя зарплата всех сотрудников', round(average, 2))
