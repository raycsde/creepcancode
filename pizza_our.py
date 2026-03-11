for_pizza = ['apizza', 'bpizza', 'cpizza']
for fpiz in for_pizza:
    print(fpiz.title())
    print(f'I like {fpiz.title()} pizza!\n')

print('I really like pizza!')

friend_pizzas = for_pizza[:]
for_pizza.append('dpizza')
friend_pizzas.append('xpizza')

print('My favorite pizzas are:')
for mf_pizza in for_pizza:
    print(mf_pizza)

print("My friend's favorite pizzas are:")
for mff_pizza in friend_pizzas:
    print(mff_pizza)
