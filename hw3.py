# File:         HW3.py
# Author:       Rachael Birky
# Date:         02.21.2012
# Section:      02
# E-mail:       rbirky1@umbc.edu
# Description:  This program will take the CMSC major classes
#               the user has taken and returns a list of classes still needed

def main():

    import string
    
    # Declare empty list for classes the user has taken
    classesTaken = []

    # Lists of required classes
    classesRequiredA = ['CMSC 201', 'CMSC 202', 'CMSC 203', 'CMSC 304',
                       'CMSC 313', 'CMSC 331', 'CMSC 341', 'CMSC 345',
                       'CMSC 411', 'CMSC 421', 'CMSC 441']

    classesRequiredB = ['MATH 151', 'MATH 152', 'MATH 221']

    classesRequiredC = ['STAT 355','STAT 451']

    # Declare empty lists for classes needed
    classesNeededA = []
    classesNeededB = []
    
    # Welcome user. Describe program.
    print "\nWelcome to Credit Counter!"
    print "This program will tell you which classes you need to take"
    print "to fulfill the CMSC major requirements."

    # Prompt user for number of classes. This variable is used for a for loop
    numClasses = input("\nHow many CS program classes have you taken? ")

    print "\nEnter each class below in the form <MAJOR-CODE> <COURSE-NUMBER>:"

    # Prompt user for each class in the format <Major Code> <Course Number>
    for i in range(numClasses):
        #Store class in variable userClass
        userClass = raw_input("Class: ")
        #Add userClass to the list classesTaken; Accept lowercase
        classesTaken.append(string.upper(userClass))

    # Loop through part A requirements to see which classes are not in
    #  the list of classes the user has taken
    for i in classesRequiredA:
        if i not in classesTaken:
            classesNeededA.append(i) # Add classes needed to list

    #Print list of classes needed for part A
    print "\nPart A requirements:"
    if classesNeededA == []:
    #If all classes taken (an empty list), print "satisfied"
        print "You have satisfied the Part A requirements."
    else:
    #If the user still has classes to take, print them using a loop
        for i in range(len(classesNeededA)):
            print "You need to take " + classesNeededA[i]

    # Loop through part B requirements to see which classes are not in
    #  the list of classes the user has taken
    for i in classesRequiredB:
        if i not in classesTaken:
            classesNeededB.append(i) # Add classes needed to list

    #Print list of classes needed for part B
    print "\nPart B requirements:"
    if classesNeededB == []:
    #If all classes taken (an empty list), print "satisfied"
        print "You have satisfied the Part B requirements."
    else:
    #If the user still has classes to take, print them using a loop
        for i in range(len(classesNeededB)):
            print "You need to take " + classesNeededB[i]

    #Print part C requirements
    print "\nPart C Requirements: "
    #Check if user has taken STAT 355 or STAT 451
    if (classesRequiredC[0] in classesTaken) or (classesRequiredC[1] in classesTaken):
        #If either, print "satisfied"
        print "You have satisfied the Part C requirements"
    else:
    #If neither, print "take STAT355 or STAT 451"
        print "You need to take ",
        print classesRequiredC[0] + ' or ' + classesRequiredC[1]

    print "\nThank you for using Credit Counter! Goodbye!\n"

main()
