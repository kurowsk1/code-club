from math import pi
from sys import exit

def intCheck (input):
  if not str.isdigit(input):
    exit("Invalid entry")
  else:
    return int(input)

def areaCircle (x):
  x = intCheck(x)
  return pi*x**2

def main ():
  radius = input(">Enter circle radius in meters: ")
  area = areaCircle(radius)
  print ("The area of a circle with a radius of", radius, "meters is", area, "square meters")

main()