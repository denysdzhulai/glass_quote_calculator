import time

width = float(input('What is the width of SU?\n'))
height = float(input('What is the height of SU?\n'))
number_of_panes = int(input('How pany panes the SU has?\n'))
labor_cost = 175


def quote_calculator(width, height, number_of_panes):
    square_of_sealed_unit_inches = round(width * height, 2)
    square_of_sealed_unit_feet = round(
        square_of_sealed_unit_inches * 0.00694, 2)
    price_per_square_feet = 0

    if square_of_sealed_unit_feet <= 8:
        price_per_square_feet = 16
    elif 7 < square_of_sealed_unit_feet <= 10:
        price_per_square_feet = 18
    elif 10 < square_of_sealed_unit_feet <= 12:
        price_per_square_feet = 18
    elif 12 < square_of_sealed_unit_feet <= 14:
        price_per_square_feet = 20
    elif 14 < square_of_sealed_unit_feet <= 18:
        price_per_square_feet = 21
    else:
        price_per_square_feet = 23

    quote_for_sealed_unit = round(
        square_of_sealed_unit_feet * price_per_square_feet, 2)

    if number_of_panes == 2:
        quote_for_sealed_unit = round(quote_for_sealed_unit * 0.8, 2)
        print('===================================')
        print(
            f'\nCalculating the quote for DOUBLE pane sealed unit with {square_of_sealed_unit_feet} square feet...')
        time.sleep(1)
        print(f'\nThe price for square feet is ${price_per_square_feet}\n')
        print('===================================')
        time.sleep(2)
        print(f'\nThe price for SU is ${quote_for_sealed_unit}\n')
        print('+ measurements and installation\n')
        print('===================================')
        time.sleep(3)
        print(
            f'\nThe quote for the customer is ${round(quote_for_sealed_unit + labor_cost, 2)} + GST')
        print('\nDo not forget to send an installer for accurate measurements!')
    elif number_of_panes == 3:
        print('===================================')
        print(
            f'\nCalculating the quote for TRIPLE pane sealed unit with {square_of_sealed_unit_feet} square feet...')
        time.sleep(1)
        print(f'\nThe price for square feet is ${price_per_square_feet}\n')
        print('===================================')
        time.sleep(2)
        print(f'\nThe price for SU is ${quote_for_sealed_unit}\n')
        print('+ measurements and installation\n')
        print('===================================')
        time.sleep(3)
        print(
            f'\nThe quote for the customer is ${round(quote_for_sealed_unit + labor_cost, 2)} + GST')
        print('\nDon\'t forget to send the installer for accurate measurements!')
    else:
        print('There can be only triple or double glazed insulated units!')

    time.sleep(2)
    print('\n***')
    input('\nPress ENTER to exit')


quote_calculator(width, height, number_of_panes)
