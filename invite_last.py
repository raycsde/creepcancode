#ray2026mar7 invite more guests to my dinner.Finnally delete everyone in my guest list.
my_guests = []
my_guests.append('Jay Chou')
print(f'Hey, {my_guests[0]}. Will you come to my dinner?')
my_guests.append('Mark Zuckerberg')
my_guests.append('Steven Jobs')
print(f'Hey, {my_guests[1]} and {my_guests[-1]}. Will you come to my dinner?')

guest_notime = my_guests.pop(0)
print(f"It's a pity that {guest_notime} can't come to my dinner!")

my_guests.insert(0, 'Elon Musk')
print(f'Hey, {my_guests[0]}, {my_guests[1]} and {my_guests[-1]}. Will you come to my dinner?')

my_guests.insert(0, 'Jack Ma')
my_guests.insert(1, 'Tony Ma')
my_guests.append('Dong')
print(f'Hey, {my_guests} Will you come to my dinner?')
print(f'Hey, {my_guests[0]}, {my_guests[1]}, {my_guests[2]}, {my_guests[3]}, {my_guests[4]} and {my_guests[-1]} Will you come to my dinner?')

print('I can only invite two people to my dinner.')
pop_gue1 = my_guests.pop()
print(f'Sorry {pop_gue1}, I cannot invite you to my dinner because the new table cannot be there.')
pop_gue2 = my_guests.pop()
print(f'Sorry {pop_gue2}, I cannot invite you to my dinner because the new table cannot be there.')
pop_gue3 = my_guests.pop()
print(f'Sorry {pop_gue3}, I cannot invite you to my dinner because the new table cannot be there.')
pop_gue4 = my_guests.pop()
print(f'Sorry {pop_gue4}, I cannot invite you to my dinner because the new table cannot be there.')
print(f'Hey {my_guests[0]}, you are in my guest list.')
print(f'Hey {my_guests[-1]}, you are in my guest list.')
del my_guests[0]
del my_guests[0]
print(my_guests)
