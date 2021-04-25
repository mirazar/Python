import re
my_dict = {}
with open('6.txt', 'r', -1, 'utf-8') as f:
    for line in f:
        name = line.split()[0]
        nums = re.findall(r'\d+', line)
        nums = [int(i) for i in nums]
        my_dict[name] = sum(nums)
print(my_dict)
