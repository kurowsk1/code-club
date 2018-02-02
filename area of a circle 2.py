from math import pi
from sys import exit

def intCheck (input):
  #Creates a new function called intCheck.  
  ##What is the convention here with function naming: the 'int' is lowercase, but the 'Check' is capitalised.  Why?
  if not str.isdigit(input):
    #'if the string entered is not numerical, then...'
   ##Speaking of which, why is the 'then' function not necessary here?
  ##Why would it be a string that is entered and not a an integer or a float?  
  ##If it is a string, the program wouldn't recognise it as a numerical value anyway.
    exit("Invalid entry")
    #Exits the program and prints 'invalid entry'.  
    ##Would this mean that you have to run the program again, or would it just take you back to the start?
  else:
    return int(input)
  #A return statement ends the execution of the function call and "returns" the result
  #If there is no return statement in the function code, the function ends, when the control flow reaches the end of the 
  #function body and the value "None" will be returned

def areaCircle (x):
  #Defines the function 'areaCircle' and assigns the inputted value to the variable 'x'.
  ##So it is not necessary to state that the value for 'x' must be input by the user?
  x = intCheck(x)
  #Subjects the variable 'x' to the intCheck function
  return pi*x**2
#Performs the pi*r-squared calculation and returns the result

def main ():
  #Defines the main function of the program
  radius = input(">Enter circle radius in meters: ")
  #Prints the text in quotations as a prompt on screen and assigns the entered value to the variable 'radius'.
  area = areaCircle(radius)
  #Performs the intCheck function and then the pi*r-squared caulculation on the entered value
  #and assigns the result to the variable 'area'.
  print ("The area of a circle with a radius of", radius, "meters is", area, "square meters")
  #Prints a human-readable output with the radius and area.

main()
#Executes the main function.
