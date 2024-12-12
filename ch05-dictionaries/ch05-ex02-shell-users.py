print('Welcome to the Shell Users Count App')
shell_count = {}
with open('./ch05-dictionaries/files/passwd') as file_in:
    for line in file_in:
        fields = line.rstrip().split(":")
        shell = fields[6]
        if shell in shell_count:
            count = shell_count[shell]
            count+=1
            shell_count[shell] = count
        else:
            # ignore empty entry
            #if shell.rstrip() != '':
            shell_count[shell] = 1

print('Shell Count Summary:')
print('====================')
print(f'{"Shell":20} {"Count"}')
print(f'{"-"*20} {"-----"}')
for shell, count in shell_count.items():
    print(f'{shell:20} {count}')
print('Bye')