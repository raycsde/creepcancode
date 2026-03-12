user_list = ['admin', 'aa', 'bb', 'cc', 'dd']
for users in user_list:
    if users == 'admin':
        print(f'Hello {users}, would you like to see a status report?')
    else:
        print(f'Hello {users}, thank you logging in again.')
if user_list:
    for users in user_list:
        print(f'Hey {users}!')
else:
    print('We need to find some users!')
    
del user_list[:]
if user_list:
    for users in user_list:
        print(f'Hey {users}!')
else:
    print('We need to find some users!')


