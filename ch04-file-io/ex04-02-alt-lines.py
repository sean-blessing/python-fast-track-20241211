print('Welcome to alt lines')
with open('./ch04-file-io/data/alt.txt') as file_in:
    with open('./ch04-file-io/data/a.txt', "w") as a_out:
        with open('./ch04-file-io/data/b.txt', "w") as b_out:
            for line in file_in:
                if line.startswith('a'):
                    a_out.write(line)
                else:
                    b_out.write(line)

print('bye')