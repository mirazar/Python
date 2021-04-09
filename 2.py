def func_user_info():

    user_info = {'name': '', 'surname': '', 'year': '',
                 'city': '', 'email': '', 'phone': ''
                 }
    for k in user_info.keys():
        user_info[k] = input(f'Введите {k}: ')
    return list(user_info.values())


print(func_user_info())
