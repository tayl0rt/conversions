"""
Temperature Converter - A program to convert F to C, and C to F

2014 Taylor Thompson
Version: 1.0 (stable)
"""
print 'Welcome to Temperature Converter!'

def celConvert():
    try:
        fahrenheit = int(raw_input('Please enter the degrees in F '))
        celOne = fahrenheit - 32
        celTwo = celOne * 5
        celThree = celTwo / 9
        print fahrenheit, 'fahrenheit is', celThree, 'degrees celcius!'
    except ValueError:
        print 'Oops, you have to enter a number!'
    return

def fahrenConvert():
    try:
        celcius = int(raw_input('Please enter the degrees in C '))
        fahrenOne = celcius * 9
        fahrenTwo = fahrenOne / 5
        fahrenThree = fahrenTwo + 32
        print celcius, 'celcius is', fahrenThree, 'degrees fahrenheit!'
    except ValueError:
        print 'Oops, you have to enter a number!'
    return


#Begin Loop
done = False
while not done:

#App Intro
    selectOption = raw_input('Please select f (fahrenheit), c (celcius) or q (quit) ')


    if selectOption == 'f':
        celConvert()

    elif selectOption == 'c':
        fahrenConvert()

    elif selectOption == 'q':
        done = True

    else:
        print 'sorry I don\'t know what you mean! please type y/n'