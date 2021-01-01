MAX_CYCLES = 1000

# Aria with Diverse Variations (pg 401)
def isWondrous(number):
    output = number
    cycle = 1

    # Run until we have proof that the number is wondrous or we have hit the max number of cycles allowed
    while output != 1 and cycle <= MAX_CYCLES:
        if output % 2 == 0:
            number_type = 'EVEN'
            output = output / 2
        else:
            number_type = 'ODD'
            output = 3 * output + 1

        print(f'Cycle {cycle}: Number is {number_type} and new number is: {output}')
        cycle = cycle + 1

    if output == 1:
        print('WONDROUS')
    else:
        print('UNWONDROUS')
