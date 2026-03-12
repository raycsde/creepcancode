favorite_fruits = []
favorite_fruits.append('apple')
favorite_fruits.append('orange')
favorite_fruits.append('banana')
print(favorite_fruits)
apple_fruit = 'apple'
if apple_fruit in favorite_fruits:
    print(f'You really like {apple_fruit}!')
if 'orange' in favorite_fruits:
    print(f'You really like orange!')
if 'banana' in favorite_fruits:
    print(f'You really like banana!')
if 'pear' not in favorite_fruits:
    print(f'You really dislike pear!')
else:
    print('WOW~')
