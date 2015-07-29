#File:       hw8.py
#Author:     Rachael Birky
#Date:       04.10.12
#Section:    02
#E-mail:     rbirky1@umbc.edu
#Description:This program converts time, temperature, and currency
#               given the original values and location of user
#               (London,Stockholm, Tampere, Helsinki, or St. Petersburg


TIME = 1
CURRENCY = 2
TEMPERATURE = 3
QUIT = 4

MAIN_MENU_MIN = TIME
MAIN_MENU_MAX = QUIT

MIN_HRS = 0
MAX_HRS = 23

MIN_MIN = 0
MAX_MIN = 59

LOCATION_CHOICES = ["L", "S", "T", "H", "P"]

LONDON_HRS = 5
STOCKHOLM_HRS = 6
TAMPERE_HRS = 7
HELSINKI_HRS = TAMPERE_HRS
ST_PETE_HRS = 8

POUNDS = 1.53730
KRONORS = 0.139083
EUROS = 1.34960
RUBLES = 0.0343348

TWELVE_HR = 12
TWENTY_FOUR_HR = 23

# input: none
# output: none (prints a greeting)
# printGreeting() displays a suitable greeting to the user
def printGreeting():
    print "Welcome to the 'World Traveler'program.\
This program will convert time, currency, and temperature\
for specific areas."

# input: none
# output: none (prints the main menu with conversion types
# displayMainMenu() displays the main menu choices
def displayMainMenu():
    print "\nWhat would you like to convert?"
    print "\n\t1 - Time\n\t2 - Currency\n\t3 - Temperature\n\t4 - Quit"
    print

# input: none
# output: none (print the location menu)
# displayLocationsMenu() displays the location menu choices
def displayLocationsMenu():
    print "\nChoose a location or M to return to Main Menu"
    print "\n\tL - London\n\tS - Stockholm\n\tT - Tampere"
    print "\tH - Helsinki\n\tP - St. Petersburg"
    print "\tM - Return to Main Menu"
    print


# input: none
# output: none (prints the converted time by calling getValidTime()
#          and foreignTimeToEastern())
# convertTime() handles all of the user input, processing,
#  and output dealing with converting time
def convertTime():
    print

    #get user input
    displayLocationsMenu()
    location = raw_input("Enter location or M to return to Main Menu: ")
    location = location.upper()

    #validation loop
    while (location not in LOCATION_CHOICES) and (location != "M"):
        print "\n*%s is not a valid choice. Try again." % (location)
        #display menu again and get user input
        displayLocationsMenu()
        location = raw_input("Enter location or M to return to Main Menu: ")
        location = location.upper()

    #loop through options and results as long as user selects valid choice
        #when M is entered, go to main menu
    while (location in LOCATION_CHOICES) and (location != "M"):
        #validate time
        timeTuple = getValidTime()

        #call conversion function, assign return values to variables,
        # print appropriate statement
        if (location == "L"):
            #*****************************************************
            #* These statement will not fit within 80 characters *
            #*     and still retain variable name meaning!!      *
            #*****************************************************
            estHr, estMin, abbrev = foreignTimeToEastern(timeTuple[0], timeTuple[1], LONDON_HRS)
            print "%d:%02d in London is %d:%02d %s EST" % (timeTuple[0],timeTuple[1],estHr,estMin,abbrev)
        elif (location == "S"):
            estHr, estMin, abbrev = foreignTimeToEastern(timeTuple[0], timeTuple[1], STOCKHOLM_HRS)
            print "%d:%02d in Stockholm is %d:%02d %s EST" % (timeTuple[0],timeTuple[1],estHr,estMin,abbrev)
        elif (location == "T"):
            estHr, estMin, abbrev = foreignTimeToEastern(timeTuple[0], timeTuple[1], TAMPERE_HRS)
            print "%d:%02d in Tampere is %d:%02d %s EST" % (timeTuple[0],timeTuple[1],estHr,estMin,abbrev)
        elif (location == "H"):
            estHr, estMin, abbrev = foreignTimeToEastern(timeTuple[0], timeTuple[1], HELSINKI_HRS)
            print "%d:%02d in Helsinki is %d:%02d %s EST" % (timeTuple[0],timeTuple[1],estHr,estMin,abbrev)
        elif (location == "P"):
            estHr, estMin, abbrev = foreignTimeToEastern(timeTuple[0], timeTuple[1], ST_PETE_HRS)
            print "%d:%02d in St. Petersburg is %d:%02d %s EST" % (timeTuple[0],timeTuple[1],estHr,estMin,abbrev)

        #get user input again
        displayLocationsMenu()
        location = raw_input("Enter location or M to return to Main Menu: ")
        location = location.upper()
        

        #validation
        while (location not in LOCATION_CHOICES) and (location != "M"):
            print "\n*%s is not a valid choice. Try again." % (location)
            #display menu again and get user input
            displayLocationsMenu()
            location = raw_input("Enter location or M to return to Main Menu: ")
            location = location.upper()
        

# input: none
# output: none (prints converted currency by calling getPositiveReal()
#          and foreignToDollars())
# convertCurrency() handles all of the user input, processing,
#  and output dealing with converting currency
def convertCurrency():
    print

    #get user input
    displayLocationsMenu()
    location = raw_input("Enter location or M to return to Main Menu: ")
    location = location.upper()

    #validation loop
    while (location not in LOCATION_CHOICES) and (location != "M"):
        #validation warning
        print "\n*%s is not a valid choice. Try again." % (location)
        #display menu again and get user input
        displayLocationsMenu()
        location = raw_input("Enter location or M to return to Main Menu: ")
        location = location.upper()

    #loop through options as long as user selects valid choice
        #when M is entered, go to main menu
    while (location in LOCATION_CHOICES) and (location != "M"):

        #ask appropriate question, call conversion function and print result
        if (location == "L"):
            amount = getPositiveReal("How many pounds? ")
            usd = foreignToDollars(amount, POUNDS)
            print "\n%.2f pounds is $%.2f" % (amount, usd)
        elif (location == "S"):
            amount = getPositiveReal("How many Kronors? ")
            usd = foreignToDollars(amount, KRONORS)
            print "\n%.2f kronors is $%.2f" % (amount, usd)
        elif (location == "T" or location == "H"):
            amount = getPositiveReal("How many Euros? ")
            usd = foreignToDollars(amount, EUROS)
            print "\n%.2f euros is $%.2f" % (amount, usd)
        elif (location == "P"):
            amount = getPositiveReal("How many Rubles? ")
            usd = foreignToDollars(amount, RUBLES)
            print "\n%.2f rubles is $%.2f" % (amount, usd)

        #get user input
        displayLocationsMenu()
        location = raw_input("Enter location or M to return to Main Menu: ")
        location = location.upper()
    
        #validation loop
        while (location not in LOCATION_CHOICES) and (location != "M"):
            #validation warning
            print "\n*%s is not a valid choice. Try again." % (location)
            #display menu again and get user input
            displayLocationsMenu()
            location = raw_input("Enter location or M to return to Main Menu: ")
            location = location.upper()
        

# input: celius value as a float
# output: none (prints converted farenheit value as float)
# convertTemp() handles all of the user input, processing,
#  and output dealing with converting temperature
def convertTemp(celsius):
    farenheit = celsiusToFarenheit(celsius)
    print "\n%.1f degrees C is %.1f degrees F" % (celsius, farenheit) 


# input: hour int, minute int, hour adjustment int
# output: returns adjusted hour as estHour int, minute alias estMin
#          and appropriate AM or PM abbreviation
# foreignTimeToEastern() changes the hour in 24 hour format
#  by the adjustment amount passed into EST in 12 hour format
#  with appropriate AM or PM
def foreignTimeToEastern(hour, minute, adjustment):
    print
    #adjust time for time zone
    estHour = hour - adjustment

    #if the 24 time adjusted is greater than 24, loop around
    if estHour < 0:
        estHour += TWENTY_FOUR_HR

    #if time is less than 12, it is AM
        #does not need conversion to 12 time
    if (estHour < TWELVE_HR):
        abbrev = "AM"
    else:
        abbrev = "PM"
        #convert to twelve hour time
        estHour = estHour - TWELVE_HR

    if (estHour == 0):
        estHour = 12
        
    #minutes do not change
    estMin = minute
    return estHour, estMin, abbrev


# input: units, conversion factor float
# output: converted currency as a float
# foreignToDollars() accepts the number of units of a foreign currency
#  and a conversion factor and returns the equivalent number of US dollars
def foreignToDollars(units, conv):
    return units * conv


# input: celcius value as a float
# output: celcius converted to farenheit float
# celsiusToFarenheit() returns the fahrenheit equivalent
#  of the celsius temperature passed in
def celsiusToFarenheit(celsius):
    farenheit = celsius * 1.8 + 32
    return farenheit


# input: none
# output: hour and minute ints in a tuple called timeTuple
# getValidTime() returns a time between 00:00 and 23:59,
#  inclusive, as an hour, minute tuple
def getValidTime():
    print "\nWhat time is it?\n"
    hour = getValidInt("Enter the hour (0 - 23): ", MIN_HRS, MAX_HRS)
    minute = getValidInt("Enter the minute (0 - 59): ", MIN_MIN, MAX_MIN)
    timeTuple = hour, minute
    return timeTuple


# input: question str, MIN int, MAX int
# output: loops until valid input is received, then returns the valid input
# getValidInt() prompts the user and gets an integer from the user
#  between min and max, inclusive and returns that valid integer
def getValidInt(question, MIN, MAX):
    choice = MAX + 1
    while (choice > MAX) or (choice < MIN):
        choice = input(question)
        if (choice > MAX) or (choice < MIN):
            print "\n*%d isn't a valid choice. Try again.*" % (choice)
    return choice


# input: question str
# output: loops until valid amount is entered, then returns the valid amount
# getPositiveReal() prompts the user and returns a positive float
def getPositiveReal(question):
    print
    amount = -1.0
    while (amount < 0):
        amount = input(question)
        if (amount < 0):
            print "\n*%.2f is not a valid choice. Try again.*" % (amount)
        
    return amount


def main():
    printGreeting()
    choice = TIME
 
    while (choice != QUIT):
        displayMainMenu()
        choice = getValidInt("Your Choice (1-4): ", MAIN_MENU_MIN, MAIN_MENU_MAX)

        #call appropriate functions for each menu choice
        if (choice == TIME):
            convertTime()
        elif (choice == CURRENCY):
            convertCurrency()
        elif (choice == TEMPERATURE):
            celsius = input("\nWhat is the Celsius temperature? ")
            convertTemp(celsius)
        elif (choice == QUIT):
            print "Goodbye!"
 
main()
