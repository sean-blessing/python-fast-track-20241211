from potus import get_info

def main():
    print('Welcome to the POTUS App')
    print('Enter the term # to retrieve a president.')
    print('Enter 0 to quit.\n')
    while True:
        term_nbr = input('Enter term #: ')
        if (term_nbr=='0'):
            break
        president = get_info(term_nbr)
        if president == None:
            print(f'No president found for term: {term_nbr}')
        print("President: ", president)
        print()
    print('Bye')

if __name__ == '__main__':
    main()