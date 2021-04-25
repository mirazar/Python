numbers = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open('number.txt', 'r', -1, 'utf-8') as f:
    with open('new_number.txt', 'w+', -1, 'utf-8') as file:
        for line in f:
            num = line.split()
            result = num[0]
            new_line = line.replace(result, numbers[result])
            file.write(new_line)
        file.seek(0)
        print(file.read())
