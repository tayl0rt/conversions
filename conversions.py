"""
Temperature Converter - A program to convert F to C, and C to F

2014 Taylor Thompson
Version: 1.0 (stable)
"""
print 'Welcome to Temperature Converter!'

def cel_convert():
    try:
        fahrenheit = int(raw_input('Please enter the degrees in F '))
        cel_one = fahrenheit - 32
        cel_two = cel_one * 5
        cel_three = cel_two / 9
        print fahrenheit, 'fahrenheit is', cel_three, 'degrees celcius!'
    except ValueError:
        print 'Oops, you have to enter a number!'
    return

def fahren_convert():
    try:
        celcius = int(raw_input('Please enter the degrees in C '))
        fahren_one = celcius * 9
        fahren_two = fahren_one / 5
        fahren_three = fahren_two + 32
        print celcius, 'celcius is', fahren_three, 'degrees fahrenheit!'
    except ValueError:
        print 'Oops, you have to enter a number!'
    return


#Begin Loop
done = False
while not done:

#App Intro
    selectOption = raw_input('Please select f (fahrenheit), c (celcius) or q (quit) ')


    if selectOption == 'f':
        cel_convert()

    elif selectOption == 'c':
        fahren_convert()

    elif selectOption == 'q':
        done = True

    else:
        print 'sorry I don\'t know what you mean! please type y/n'