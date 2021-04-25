with open('my_file.txt', 'r', -1, 'utf-8') as f:
    count = 0
    for line in f:
        count += 1
        text = len(line.split())
        print(f'В {count} строке, {text} слов')
print(f'В тексте {count} строк')