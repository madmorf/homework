inpt = input('\nEnter your age:\n')

digit = inpt.isdigit()

if digit != True:
    print('\nWrong input, try numeral!')
else:
    if int(inpt) < 18:
        print('\nYou are too small')
    else:
        print('\nYou are Ok!')