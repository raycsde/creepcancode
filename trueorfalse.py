car = ['acar', 'bcar',' ccar', 'dcar']
print(car[0] == 'x')
print(car[0] == 'acar')

bike = 'abike'
if bike == 'abike':
    print(f'The bike is {bike.title()}.')

if bike != 'bbike':
    print('The is not a bbike!')

if bike in car:
    print('wow!')
elif bike == 'abike':
    print('cool!')
else:
    print('no!')

age1 = 10
if age1 >= 11:
    print('fine.')
else:
    print('no!')

age2 = 11
age3 = 12
print(age2 == 10)
print(age2 == 11 and age3 == 12)
print(age2 == 11 or age3 ==15)

newcar = 'acar'
print(newcar in car)
if newcar not in car:
    print('What?')
else:
    print("Yes!")