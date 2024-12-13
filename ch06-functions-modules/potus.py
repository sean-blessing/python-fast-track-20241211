def get_info(term):
    # find the president by term nbr
    with open('./ch06-functions-modules/files/presidents.txt') as file_in:
        president = None
        for line in file_in:
            # fields = line.rstrip().split(":")
            # print(f'fields: {fields}')
            term_nbr, last_name, first_name, term_start, term_end, \
                birth_place, birth_state, birth_date, death_date, \
                party = line.rstrip().split(":")
            if term_nbr == term:
                # create dictionary for this tuple
                president = {'term': term_nbr, 'last_name': last_name,
                             'first_name': first_name, 'term_start': term_start,
                             'term_end': term_end, 'birth_place': birth_place,
                             'birth_state': birth_state, 'birth_date':birth_date, 
                             'death_date': death_date, 'party': party }
                break
        return president
            