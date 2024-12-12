print('Welcome to Dictionaries')
kv_pairs = [(1,'January'), (2, 'February'), (3, 'March')]
months = dict(kv_pairs)
print(f'months = {months}')
months[4] = 'April'
print(f'months = {months}')
months[4]= 'May'
print(f'months = {months}')
months.pop(4)
print(f'months = {months}')

states_dict = {'OH': 'Ohio', 'KY': 'Kentucky', 'IN': 'Indiana', 'MI': 'Michigan'}
print(f'states_dict = {states_dict}')
states_dict['CO'] = 'Colorado'
print(f'states_dict = {states_dict}')

# check for existence

print(f'CO?: {'CO' in states_dict}')
print(f'FL?: {'FL' in states_dict}')

print(f'OH={states_dict['OH']}')
# print(f'FL={states_dict['FL']}')
print(f'FL={states_dict.get('FL')}')
print(f'FL={states_dict.get('FL', 'Not Defined')}')

if 'FL' not in states_dict:
    print('Key does not exist')

print('\nIterate over a dictionary')
print(f'states_dict keys: {states_dict.keys()}')
print(f'states_dict values: {states_dict.values()}')
print(f'states_dict items: {states_dict.items()}')

for state, state_name in states_dict.items():
    print(f'[{state}]: {state_name}')
    
for state, state_name in sorted(states_dict.items()):
    print(f'[{state}]: {state_name}')
    
knight_info = {}

with open('./ch05-dictionaries/files/knights.txt') as file_in:
    for line in file_in:
        name, title, color, quest, comment = line.rstrip().split(':')
        knight_info[name] = title, color, quest, comment

for name, values in knight_info.items():
    print(f'Knight: {name}, values={values}')
print('Bye')