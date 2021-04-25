import json

sum_profit = 0
count = 0
my_dict = [dict(), dict()]
with open('7.txt', 'r', -1, 'utf-8') as f:
    for line in f:
        firm = line.split()

        name = firm[0]
        profit = int(firm[2]) - int(firm[3])
        if profit > 0:
            sum_profit += profit
            count += 1
        my_dict[0][name] = profit

my_dict[1]['средняя прибыль'] = sum_profit/count

with open('7.json', 'w') as f:
    json.dump(my_dict, f, indent=4)
