ctemps = [-40.0, 0.0, 37.0, 75.0, 100.0]

for cel in ctemps:
    f = ((9 * cel) / 5) + 32
    print(f'celcius: {cel}, fahrenheit: {f}')

# for i in range(len(ctemps)):
#     f = ((9 * ctemps[i]) / 5) + 32
#     print(f'[{i}]: celcius: {ctemps[i]}, fahrenheit: {f}')
    
# print(f'idx 5: {ctemps[5]}')