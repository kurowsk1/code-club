import math						# this imports the math library, which contains various mathematical functions
radius = input('enter circle radius in meters')		# what follows the '=' sign assigns that value to the variable 'radius'.  The 'input' 									command lets the program know to wait for the user to input some value.  
print ('radius',radius, 'meters')			# Within the brackets, the items encapsulated in '' marks are to be printed verbatim. 									The variable 'radius' is also within the brackets, without '' marks, instructing 									the program to to print the variable's value; not the variable name.
area = math.pi*radius**2				#This defines a new variable; area.  The pi function is used from the math library and	 									it is multiplied by the square of radius.  Note the use of the ** to raise 									radius to an index of 2
print ('area is', area, 'square meters')		
