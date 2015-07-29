# File name:  hw5.py
# Author:     Rachael Birky
# Date:       03.05.2012
# Section:    02
# Email:      rbirky1@umbc.edu
# Description:This program examines positive integers in a user-given range
#             and categorizes them as odd/even, prime/composite,
#             perfect/abundant/deficient, square, and triangular

import sys
HEADER_WIDTH_MULTIPLIER = 7
CHECK_EVEN = 2
ROOT_MULTIPLIER = 0.5
MAX_VALUE = 100000

#printGreeting() greets user and explains program purpose
def printGreeting():
    print
    print "Hello! This program classifies positive integers as Odd/Even,\n\
Prime/Composite, Perfect/Abundant/Deficient, Square, and Triangular."
    print "\nYou will now get to choose the range of positive integers that\n\
you would like to see classified."
    print

#printTableHeader() creates a formatted heading for the chart
def printTableHeading():
    print "%7s     Classifications..." % ("Int")
    print "---------"*HEADER_WIDTH_MULTIPLIER

#isOdd() determines whether the integer is odd, which returns true
#input: integer n in user-given range
#output: True or False
def isOdd(n):
    return (n%CHECK_EVEN != 0)

#isPrime() determines whether the integer is prime
#input: interger n in user-given range
#output: True or False
def isPrime(n):
    isPrime = True
    #is i a factor of n and not 1 or n? then isPrime is False
    for i in range(1, n):
        if (isDivisor(n, i)) and (i != 1) and (i != n):
            isPrime = False
    return isPrime

#checkForPerfect() classifies n as "perfect", "abundant" or "deficient"
#input: integer n in user-given range
#output: string "perfect", "abundant", or "deficient"
def checkForPerfect(n):
    if (sumDivisors(n) == n):
        return "Perfect"
    elif (sumDivisors(n) < n):
        return "Deficient"
    else:
        return "Abundant"

#sumDivisors() returns the sum of the divisors of n
#input: integer n given by user
#output: summation integer
def sumDivisors(n):
    total = 0
    for i in range(1, n):
        if (isDivisor(n, i)):
            total = total + i
    return total

#isDivisor() returns True if b is a divisor of a, and False if not
#input: a and b, both user-defined integers
#output: True or False
def isDivisor(a, b):
    if (a%b == 0):
        return True
    else:
        return False

#isSquare() returns True if n is a perfect square, False if not
def isSquare(n):
    nRoot = n**ROOT_MULTIPLIER
    return int(nRoot) == nRoot
    

#isTriangular() returns True if n is a triangular number, False if not
#input: n, a user-defined integer
#output: True or False
def isTriangular(n):
    total = 0
    isTriangular = False
    #if at any point, consecutive value add to a total of n,
    # isTriangular becomes true
    for i in range(n+1):
        total = total + i
        if (total == n):
            isTriangular = True
    return isTriangular

#printTableLine() prints the info for one number on one line of the table.
#input: user integer n, results from isOdd(), isPrime(), checkForPerfect(),
#       isSquare(), and isTriangular()
#output: a formatted line of text 
def printTableLine(n, odd, prime, perfect, square, triangular):
    print "%7d     %-5s  %-10s  %-10s %-7s %-7s" % (n, odd, prime, perfect, square, triangular)

def main():
    
    printGreeting()

    #promt user for beginning integer
    print "Start with which positive integer?"
    startNum = input("Please enter an integer between 1 and 100000: ")
    #promt user for ending integer
    print "End with which positive integer?"
    endNum = input("Please enter an integer between %d and 100000: " % (startNum))


    #data verification: input are positive integers
    # and end number is greater than beginning number
    while (startNum <= 0) or (endNum <= 0) or (endNum <= startNum) or (endNum > MAX_VALUE):
        print "\nInvalid input!"
        print "Both values must be positive integers and the ending"
        print " number must be greater than the beginning number.\n"

        #promt user for beginning integer
        print "Start with which positive integer?"
        startNum = input("Please enter an integer between 1 and 100000: ")
        #promt user for ending integer
        print "End with which positive integer?"
        endNum = input("Please enter an integer between %d and 100000: " % (startNum))


    print
    printTableHeading()

    #loop through each value in range
    for n in range(startNum, endNum+1):

        #establish default parameter values
        odd = "Even"
        prime = "Composite"
        square = ""
        triangular = ""

        #edit defaults by calling functions
        if (isOdd(n)):
            odd = "Odd"
            
        if (n == 1):
            prime = "Neither"
        else:
            if (isPrime(n)):
                prime = "Prime"
                
        if (isSquare(n)):
            square = "Square"
            
        if (isTriangular(n)):
            triangular = "Triangular"

        #print current line, passing each parameter to function   
        printTableLine(n, odd, prime, checkForPerfect(n), square, triangular)
        
    print
        
main()
