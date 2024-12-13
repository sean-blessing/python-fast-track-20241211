def get_integer(prompt):
    nbr = 0
    while True:
        try:
            nbr_str = input(prompt)
            nbr = int(nbr_str)
            break
        except:
            print(f'Invalid Entry [{nbr_str}]. Try again.')
    return nbr

def get_integer_within_range(prompt, min, max):
    nbr = 0
    while True:
        nbr = get_integer(prompt)
        if nbr >= min and nbr <= max:
            break
        else:
            print(f'Invalid entry [{nbr}]: must be within range [{min} - {max}].')
    
    return nbr
