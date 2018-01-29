def main():
  motor = ["0","1","3","6"]
  # a list of possible 'motor' codes.
  pumphead = ["81","82","21","22","23","24","31","32","33","34","35","36","37","41","41T","42","42T","43","43T","46","46T","47","47T","472","46T"]
  # a list of possible 'pump head' codes.
  chemtec = []
  # creates a blank list, ready to store part numbers.
  for a in range (0, len(motor)):
  # iterates from 0 to the length of the motor list.
    for b in range (0, len(pumphead)):
    # iterates from 0 to the length of the pump head list.
      chemtec.append(''.join(["200-CHEM-1", motor[a], pumphead[b]]))
      # 'appends' each combination to the chemtec list.
  print(chemtec)
  # prints the chemtec list to terminal.

main()
# initiates the main function.