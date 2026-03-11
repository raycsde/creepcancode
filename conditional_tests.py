string_a = 'a'
string_b = 'b'
string_c = 'a'
if string_a == string_b:
    print('a=b')
if string_a != string_b:
    print('a!=b')
if string_a == string_c:
    print('cool.')

print(string_a == string_c)
print(string_b == string_c)

string_d = 'A'
if string_a.lower() == string_d.lower():
    print("It's so cool!")

list_abc = ['a', 'b', 'c']
print(string_a in list_abc)
if string_d not in list_abc:
    print(f'You should lower it: {string_d.lower()}')
