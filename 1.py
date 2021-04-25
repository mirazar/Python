with open('my_file.txt', 'w+', -1, 'utf-8') as f:
    a = None
    while a != '':
        a = input('Напишите чтонибуть \n'
                  'для выхода нажмите enter: ')
        if a == '':
            f.seek(0)
            print(f.read())
        else:
            f.write(f'{a}\n')
