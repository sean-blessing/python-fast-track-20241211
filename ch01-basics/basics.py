# This is a one line comment
# Now we'll define some variables
a = 'hello'
b = 'world'
print('Hello World!')
print(a + b)
price_1 = 15.99
month_number = 1

sentence = 'hello there. \nThis is a new line'
print(sentence)
name = 'Frank O\'Connell'
print(name)
tabbed_message = 'This message includes a\t\ttab'
print(tabbed_message)
name = """James Earle "Jimmy" Carter"""
print(name)
warning = """warning:
students may be lethargic
after lunch!
"""
print(warning)

file_location = r'c:\repos\trivera_fast_track'
print(file_location)

# euros example in unicode
print('The cost is \u20ac1.23M')

price = 11.99
quantity = 5
tax_pct = .065
total = (price * quantity) * (1+tax_pct)
print('Total: '+str(total))
print(f'Total: {total}')

print('\nMath functions')
print(f'Exponent: {quantity ** 5}')

nbr1 = 9.3

print(f'nbr1 / 3: {nbr1 / 3}')
print(f'nbr1 // 3: {nbr1 // 3}')
print(f'nbr1 % 3: {nbr1 % 3}')

x1 = 11
y1 = 35
print(x1, y1)
print(x1, end='*')
print(y1)

print(f'Total is: ${total:.2f}')

first_name = input('Enter First Name: ')
last_name = input('Enter Last Name: ')
birth_month = input('Enter Birth Month')
nbr1 = int(input('Enter number 1: '))
nbr2 = int(input('Enter number 2: '))

print(f'{last_name}, {first_name}, birth month: {birth_month}')
print(nbr1+nbr2)

# rounding: https://www.w3schools.com/python/ref_func_round.asp
print(f'Total (not rounded): {total}')
print(f'Total (rounded to 3 decimal places): {round(total, 3)}')
print(total.is_integer())
print(first_name.isnumeric())
print(first_name.isalpha())