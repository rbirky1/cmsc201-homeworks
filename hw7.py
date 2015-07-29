#File:       hw7.py
#Author:     Rachael Birky
#Date:       04.02.12
#Section:    02
#E-mail:     rbirky1@umbc.edu
#Description:This program takes a user-defined number or range, performs
#               a hailstone algorithm, and prints the resulting number
#               chain. It uses a menu to provide options for a number,
#               a range, finding the longest in a range, or quitting.
#               NOW WITH GRAPHICS


from graphics import *
import string
from time import sleep

CUT_OFF_LOWER = 1
CUT_OFF_UPPER = 10000
START_QUESTION = "Enter starting integer"
END_QUESTION = "Enter ending integer"

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500

X_NUM_RANGE = 10
Y_NUM_RANGE = 4

CORNER_BUFFER = 30
SIDE_BUFFER = 10

X_SPACING = WINDOW_WIDTH / X_NUM_RANGE
Y_SPACING = (WINDOW_HEIGHT / Y_NUM_RANGE) - SIDE_BUFFER

REC_WIDTH = 20
DRAW_AREA = WINDOW_HEIGHT - SIDE_BUFFER

#printGreeting() greets the user and explains the program purpose
#input: none
#output: string greeting
def printGreeting():
    print "Hello and welcome!"
    print "This program finds hailstone sequences of numbers you choose.\n\
If the number is even, the next number in the hailstone sequence is found by\n\
dividing by two.\n\
If it is odd, the next number is found by multiplying by three and adding one.\n"

#printMenu() prints the choices the user can make
#input: none
#output: table of options
def printMenu():
    print "\n\tI - view sequence for an Individual value\n\n\
\tR - view sequence for a Range of values\n\n\
\tL - find the Longest chain\n\n\
\tH - view a Histogram of chain lengths for a range\n\n\
\tQ - Quit"

#getValidInt() ensures the user-given values are within the desired range
#input: question (a string customized to minimum and maximum values possible,
#    minValue and maxValue (as defined by the CUTT_OFFs and user given range)
#output: returns the valid value to be saved in a variable in main()
#Source Citation: Miner, Don and Sue Evans. Class Notes: Loops. Slide 13.
#   http://www.csee.umbc.edu/courses/undergraduate/201/spring12/lectures/loops.html#(13)
def getValidInt(question, minValue, maxValue):
    #initialize value as invalid to enter loop
    value = maxValue + 1
    #create prompt for user
    prompt = question + " (" + str(minValue) + "-" + str(maxValue) + "): "
    #loop until inputted value is valid; set and return value
    while (value == '' or value < minValue or value > maxValue):
        value = raw_input(prompt)
        if len(value) != 0:
            value = int(value)
    return value
    
#hailstone() performs the hailstone algorithm to the values
#input: number to be changed
#output: prints a number chain and returns the length
def hailstone(n):
    #initialize chain as an empty string
    chain = ""
    count = 1
    #loop until n == 1, concantenate each number to chain
    while (n != 1):
        chain = chain + str(n) + " -> "
        if isOdd(n):
            n = 3 * n + 1
        else:
            n = n/2
        count = count + 1
    #when it reaches one, do not add an arrow to end
    chain = chain + str(n)
    #print resulting string
    print chain + " ; length = ", count
    #count variable used for 'L' option
    return count

#isOdd() determines if the given value is odd
#input: number n
#output: boolean True or False
def isOdd(n):
    return (n%2 != 0)


def drawHistogram(start, longestLength, lengthList):
    
    #create window of standard size
    win = GraphWin("Histogram of Chain Lengths", WINDOW_HEIGHT, WINDOW_WIDTH)
    #reset coordinates to match Cartesian plane
    win.setCoords(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
    win.setBackground("white")

    #draw x-axis, evenly spaced
    xSpacing = CORNER_BUFFER
    index = 0
    for i in range(start, start + X_NUM_RANGE):
        xAxis = Text(Point(xSpacing, SIDE_BUFFER), str(i))
        xAxis.draw(win)

        #draw rectangle for particular number
        # find bar height by using a ratio: percentage of length compared to longest
        #  then percentage of length out of drawing area
        recHeight = float(lengthList[index]) / longestLength * DRAW_AREA
        recX = xSpacing - (REC_WIDTH / 2)
        recP1 = Point(recX, recHeight)
        recP2 = Point(recX + REC_WIDTH, CORNER_BUFFER)
        rec = Rectangle(recP1, recP2)
        rec.setFill("red")
        rec.draw(win)
        
        xSpacing += X_SPACING
        index += 1
        

    #find numbers to use in y-axis scale: highest, middle, quarters
    scaleHalf = longestLength / 2
    scaleUpperQuarter = (longestLength + scaleHalf) / 2
    scaleLowerQuarter = scaleHalf / 2
    scaleList = [scaleLowerQuarter, scaleHalf, scaleUpperQuarter, longestLength]

    #draw y-axis, evenly spaced, depending on longestLength
    ySpacing = CORNER_BUFFER + Y_SPACING
    for i in range(Y_NUM_RANGE):
        yAxis = Text(Point(SIDE_BUFFER, ySpacing), str(scaleList[i]))
        yAxis.draw(win)
        ySpacing += Y_SPACING
        
    sleep(10)
    win.close()
    

def main():
    #greet user
    printGreeting()
    #initialize number with longest chain to zero
    longestChainNum = 0
    #initialize longest chain to zero in number
    longestChainCount = 0
    #initialize choice to enter while loop
    choice = ""
    while(choice!='Q'):
        printMenu()
        #get input from user
        choice = raw_input("\nEnter your choice: ")
        choice = choice.upper()

        #evaluate user choice to call correct functions
        if choice == 'I':
            n = input("Enter a number (1-10000): ")
            #n should not be one, so return to menu
            if n == 1:
                return
            #call hailstone functions for all other valid inputs
            else:
                while (n < CUT_OFF_LOWER) or (n > CUT_OFF_UPPER):
                    n = input("\n*Invalid input!*\nEnter a number (1-10000): ")
                hailstone(n)
        #get a range from user and call hailstone() the number of times needed
        # to get through all values in range (from start number to end number + 1)
        # initial start and stop are the cut offs (constants, see above)
        elif choice == 'R':
            start = getValidInt(START_QUESTION, CUT_OFF_LOWER, CUT_OFF_UPPER)
            end = getValidInt(END_QUESTION, start, CUT_OFF_UPPER)
            for n in range (start,end+1):
                hailstone(n)
        #perform the same operations as 'R' but keep track of length of chain
        # returned by hailstone()
        elif choice == 'L':
            start = getValidInt(START_QUESTION, CUT_OFF_LOWER, CUT_OFF_UPPER)
            end = getValidInt(END_QUESTION, start, CUT_OFF_UPPER)
            for n in range (start,end+1):
                currentChainCount = hailstone(n)
                #if the current chain is longer, store number and length in
                # longestChainCount and longestChainNum
                if currentChainCount > longestChainCount:
                    longestChainCount = currentChainCount
                    longestChainNum = n
            #number and count should not be zero! (the initialized value)
            # if it is, tell user there was an error and return to menu
            if longestChainNum == 0 or longestChainCount == 0:
                print "error"
                return
            else:
                print "\nThe longest chain is %d and is %d numbers long." % (longestChainNum, longestChainCount)
                hailstone(longestChainNum)
        elif choice == 'H':
            start = input("\nEnter starting value: ")
            lengthList = []

            # restrict the range to 10 values
            for n in range (start, start + X_NUM_RANGE):
                length = hailstone(n)
                lengthList.append(length)

            #find longest chain length
            longestLength = max(lengthList)

            drawHistogram(start, longestLength, lengthList)
            
                
        elif choice == 'Q':
            print "Goodbye!"
            return
        else:
            print "\n*" + choice + " is not a valid choice. Please choose again.*"
main()
