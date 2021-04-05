seasons = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето'
           'лето', 'осень', 'осень', 'осень', 'зима']
seasons = seasons[int(input('Введите номер месяца: ')) - 1]
print(seasons)

seasons = {'зима': [12, 1, 2],
           'весна': [3, 4, 5],
           'лето': [6, 7, 8],
           'осень': [9, 10, ]}
month = int(input('Введите номер месяца: '))
for k, v in seasons.items():
    if month in v:
        print(k)
