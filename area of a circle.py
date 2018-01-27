from math import pi
from sys import exit
# this imports the math library, which contains various mathematical functions

radius = input(">Enter circle radius in meters: ")
# what follows the '=' sign assigns that value to the variable 'radius'.
# The 'input' command lets the program know to wait for the user to input 
# some value.

def intCheck (input):
    if str.isdigit(input):
      pass
    else:
      exit("Invalid entry")

intCheck(radius)

radius = int(radius)
# Converts the variable 'radius' from a string to an integer.

# print ("Radius:", radius, "meters")
# Within the brackets, the items encapsulated in '' marks are to be
# printed verbatim.The variable 'radius' is also within the brackets,
# without '' marks, instructing the program to to print the variable's
# value; not the variable name.

area = pi*radius**2
# This defines a new variable; area. The pi function is used from the math
# library and it is multiplied by the square of radius. Note the use of
# the ** to raise radius to an index of 2

print("")
print ("The area of a circle with radius", radius, "is", area, "square meters")
print("")
# Prints the result