fruits = ['apple', 'cherry', 'orange', 'kiwi', 'banana', 'pear', 'fig'] # list
name = "Eric Idle"  # str
knight = 'King', 'Arthur', 'Britain'  # tuple
data = b"abcde"   # bytes

# access an element in a list:
print(f'5th fruit: {fruits[4]}')
print(f'3rd letter of name: {name[2]}')

# add an element to a list:
fruits.append('watermelon')
print(f'fruits: {fruits}')

# use some methods of List type
# index
print(f'fruits index of "pear": {fruits.index('pear')}')
fruit_removed = fruits.pop(5)
print(f'{fruit_removed} was removed.', fruits)
fruits.insert(5, 'pear')
print(f'Added "pear" again... ', fruits)
fruits.sort()
print(f'Sorted fruits = {fruits}')
fruits[5] = 'mango'
print(f'fruits = {fruits}')

print('\nSlicing fruits...')
print(f'fruits[2:]', fruits[2:])
print(f'fruits[2:5]', fruits[2:5])
print(f'fruits[2::2]', fruits[2::2])

# foreach loop - don't need index position
# loop through fruits and print each fruit in title case
for fruit in fruits:
    print(f'Fruit = {fruit.title()}')
    
# tuple
movie1 = ('Star Wars Episode IV', 1977, 'PG', 'George Lucas')
print(f'movie1', movie1)

# tuple elements - access
print(f'title = {movie1[0]}')
print(f'year = {movie1[1]}')
print(f'rating = {movie1[2]}')
print(f'director = {movie1[3]}')

# tuple unpacking
title, year, rating, director = movie1
print(f'title = {title}')
print(f'year = {year}')
print(f'rating = {rating}')
print(f'director = {director}')

# print fruits and index position
# enumerate
for i, fruit in enumerate(fruits):
    print(f'[{i}]: {fruit}')

# do this again using range
for i in range(fruits.__len__()):
    print(f'index {i} is {fruits[i]}')
