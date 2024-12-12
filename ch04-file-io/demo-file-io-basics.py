print('Welcome to File IO')

with open('./ch04-file-io/mary.txt') as file_in:
    # contents = file_in.readlines()
    # print(f'contents: {contents}')
    for line in file_in:
        line = line.rstrip()
        print(line)

print('\nWrite states to a file:')

file_name = './ch04-file-io/states.txt'
import os
os.remove(file_name+'.BAK')
os.rename(file_name, file_name + '.BAK')

states = ['Ohio', 'Indiana', 'Michigan', 'Kentucky', 'Colorado']
# write these states to a text file
with open(file_name, "w") as file_out:
    for state in states:
        file_out.write(state + "\n")
                
print('Bye')