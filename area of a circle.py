from math import pi
from sys import exit
# this imports the math library, which contains various mathematical functions

radius = input(">Enter circle radius in meters: ")
# what follows the '=' sign assigns that value to the variable 'radius'.
# The 'input' command lets the program know to wait for the user to input 
# some value.

def intCheck (input):
    if str.isdigit(input): # The str.isdigit() method is detailed here: https://www.tutorialspoint.com/python/string_isdigit.htm
      return int(input)
    else:
      exit("Invalid entry")

# Defines a function that takes an input ('input') and runs an 'if' statement.
# If the input is a 'digit', the function returns the input converted to
# an integer. If the input is not a 'digit' then the program is terminated.

radius = intCheck(radius)
# This is running the variable 'radius' through the intCheck function we defined earlier.

area = pi*radius**2
# This defines a new variable; area. The pi function is used from the math
# library and it is multiplied by the square of radius. Note the use of
# the ** to raise radius to an index of 2

print ("The area of a circle with a radius of", radius, "meters is", area, "square meters")
# Prints the result