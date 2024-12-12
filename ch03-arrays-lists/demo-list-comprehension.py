fruits = ['apple', 'cherry', 'orange', 'kiwi', 'banana', 'pear', 'fig', 'apricot']

# transform this list to uppercase - for loop
upper_fruits = []
for f in fruits:
    upper_fruits.append(f.upper())

print(f'upper_fruits = {upper_fruits}')

upper_fruits = [f.upper() for f in fruits]
print(f'upper_fruits (list comp.)= {upper_fruits}')

# a new list of fruits that start with the letter 'a'
a_fruits = []
for fruit in fruits:
    if fruit.startswith('a'):
        a_fruits.append(fruit.title())
print(f'a fruits 1: {a_fruits}')

a_fruits = [f.title() for f in fruits if f.startswith('a')]
print(f'a_fruits 2: {a_fruits}')

values = [2, 42, 18, 39.7, 92, '14', "boom", ['a', 'b', 'c']]
print(f'values original list: {values}')

# multiple each value by 2
new_values = []
for v in values:
    new_values.append(v*2)
print(f'new_values: {new_values}')

# LC - create a new list of only the numeric values multiplied by 2
new_values = [v*2 for v in values if isinstance(v, int)]
print(f'new_values ints: {new_values}')

suits = 'Clubs', 'Diamonds', 'Hearts', 'Spades'
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
deck_of_cards = []
for suit in suits:
    for rank in ranks:
        deck_of_cards.append(f'{rank} of {suit}')

print(f'deck_of_cards = ')
for c in deck_of_cards:
    print(c)

print('\n Deck of Cards - List Comprehension')        
# Use list comprehension to generate a deck of cards
deck_of_cards = [(rank, suit) for suit in suits for rank in ranks]
for c in deck_of_cards:
    print(c)
