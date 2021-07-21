pizzas = ['Chicago Style','Chicago Style','Pan Pizza']
friend_pizzas = pizzas[:]
pizzas.append('Thick style')
friend_pizzas.append('Cracker and Thin Styles')
print("My favorite pizzas are:\n")
for pizza in pizzas:
    print(pizza)
print('\n')

print("My friend's favorite pizzas are:\n")
for pizza in friend_pizzas:
    print(pizza)
