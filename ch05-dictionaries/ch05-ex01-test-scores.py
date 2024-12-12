print('Welcome to the test scores app')
student_dict = {}
with open('./ch05-dictionaries/files/testscores.dat') as file_in:
    for line in file_in:
        name, score = line.rstrip().split(':')
        student_dict[name] = int(score)
print(f'{"Student":20}{"Score":10}{"Grade":10}')
total = 0
for student, score in student_dict.items():
    total += score
    grade = 'F'
    if score >= 95:
        grade = 'A'
    elif score >= 89:
        grade = 'B'
    elif score >= 83:
        grade = 'C'
    elif score >= 75:
        grade = 'D'
    print(f'{student:20}{score:<10}{grade:10}')
#score_avg = sum(student_dict.values()) / len(student_dict)
score_avg = total / len(student_dict)
print(f'Average Score: {score_avg}')

print('Bye')