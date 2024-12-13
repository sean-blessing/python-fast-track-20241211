from validation_functions import get_integer, get_integer_within_range

def main():
    print('Welcome to the console io app')

    first_name = input('Enter first name: ')
    last_name = input('Enter last name: ')

    print('Enter two whole numbers I can add:')

    # get nbr1
    nbr1 = get_integer('Enter a whole number: ')

    # get nbr2
    nbr2 = get_integer('Enter another whole number: ')

    # get integer logic AND validate within a range
    month_number = get_integer_within_range('Enter current month number: ', 1, 12)
            
    print(f'You entered: {first_name}, {last_name}, {nbr1}, {nbr2}, {month_number}')
    print(f'Sum = {nbr1 + nbr2}')

    print('Bye')

if __name__ == '__main__':
    main()