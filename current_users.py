current_users = ['a1', 'b2', 'C3', 'D4', 'e5']
new_users = ['a1', 'c3', 'h4', 'kk9', 'E5']
current_usersfk = [cuk.lower() for cuk in current_users]
for nu in new_users:
    if nu.lower() in current_usersfk:
        print(f'Please enter a new user id, {nu} has been used.')
    else:
        print(f'{nu} is never been used. You can use it.')
