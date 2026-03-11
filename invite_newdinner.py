#ray2026mar6 invite_newdinner.py Oops, Jay Chou doesn't have time, maybe I can invite Elon Musk?
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
