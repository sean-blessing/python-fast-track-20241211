import csv

with open ('./ch16-csv/files/knights.csv') as file_in:
    knight_rdr = csv.reader(file_in)
    
    for name, title, color, quest, comment, number, ladies in knight_rdr:
        print(f'{title:4s} {name:9s} {quest}')

print('\n Presidents CSV')
field_names = ['term', 'firstname', 'lastname', 'birthplace', 'state', 'party']

with open('./ch16-csv/files/presidents.csv') as file_in:
    presidents_rdr = csv.DictReader(file_in, fieldnames=field_names)
    for row in presidents_rdr:
        print(f'{row['firstname']:25} {row['lastname']:12} {row['party']}')