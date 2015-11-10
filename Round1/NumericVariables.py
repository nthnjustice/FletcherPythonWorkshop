a = 123 #assigns the integer value 123 to a variable named "a"
b = 222

print a + b #prints: 345

c = a + b

print c #prints: 345

############################################################################

a = 1.5 #assigns the new floating-point value 1.5 to the variable "a"

print a * 4 #prints decimal product: 6.0

############################################################################

d = 2 ** 3 #exponent notation, assigns integer 2^3 to the variable "d" 

print d #prints: 8

############################################################################

a = 7/3 #assigns the integer value of 2 to the variable "a",
          #remainder is ignored

b = 7%3 #assigns the remainder of 7/3 to the variable "b"

print "7/3 equals " + str(a) + " with a remainder of " + str(b)
#calling the function "str()" converts whatever is between the parentheses
  #into a string - useful for printing concatenated statements 

############################################################################

import math #open the biult-in module called math

print math.pi #prints the "pi" object located in the "math" module

a = math.sqrt(9) #calls the "sqrt()" function in the "math" module
                  #to find the square-root of 9

print a #prints: 3

############################################################################

import random #open the built-in module called random

print random.random() #calls the "random()" function in the "random" module
                        #and prints a random number

print random.choice([1, 2, 3, 4]) #Prints a random number from the
                                    # collection "[1, 2, 3, 4]"

