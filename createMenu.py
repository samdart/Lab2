#
def createMenu(optionList):
  """
  Precondition:optionList is a list of strings
  Postcondition: each item in optionList is printed with formatting
  Description: Prints a list of stringss in a menu format
  """
  tmp = ' '; ct = 0
  for opt in optionList:
    tmp += str(ct) + '.' + opt + '\n'
    ct += 1
  return tmp
