# traffic light example
# prompt for light_color until user enters 'x'
#while True:
light_color = ''
while light_color != 'x':
    light_color = input('Traffic Light Color: ').lower()
    # red - stop, green - go, yellow - slow down
    if light_color == 'green':
        print("Go!")
    elif light_color == 'yellow':
        print("Slow down")
    elif light_color == 'red':
        print("Stop")
    elif light_color == 'x':
        print('x')
    else:
        print("Invalid light color")

# conditional expression
# given a number, evaluate if it is even or odd
# return the message 'even' or 'odd'
nbr = 20
# message = ''
# if nbr % 2 == 0:
#     message = 'even'
# else:
#     message = 'odd'
message = 'even' if nbr % 2 == 0 else 'odd'
print(f'message = {message}')

# for loops and ranges
print(f'range(10): {range(11)}')
for i in range(11):
    print(i)
    
for j in range(0,101,2):
    print(f'j={j}')