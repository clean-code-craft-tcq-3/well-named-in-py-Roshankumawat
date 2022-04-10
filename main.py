MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]

def getColorFromPairNumber(pair_number):
  zero_based_pair_number = pair_number - 1
  major_index = zero_based_pair_number // len(MAJOR_COLORS)
  if major_index >= len(MAJOR_COLORS):
    raise Exception('Major index out of range')
  minor_index = zero_based_pair_number % len(MINOR_COLORS)
  if minor_index >= len(MINOR_COLORS):
    raise Exception('Minor index out of range')
  return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]
  
def getPairNumberFromColor(major_color, minor_color):
  try:
    major_index = MAJOR_COLORS.index(major_color)
  except ValueError:
    raise Exception('Major index out of range')
  try:
    minor_index = MINOR_COLORS.index(minor_color)
  except ValueError:
    raise Exception('Minor index out of range')
  return major_index * len(MINOR_COLORS) + minor_index + 1

def colorPairToString(major_color, minor_color):
  return f'{major_color} {minor_color}'

 def getColorNameAndPairNumber():
    totalNumberOfPairs= len(MAJOR_COLORS)*len(MINOR_COLORS)
    print( totalNumberOfPairs)
    for pair_number in range(totalNumberOfPairs):
        oneBasedPairNumber=pair_number+1
        return (oneBasedPairNumber, getColorFromPairNumber(oneBasedPairNumber))
def testNumberToPair(PairNumber, ExpMajorColor, ExpMinorColor):
   major_color, minor_color = getColorFromPairNumber(PairNumber) # noqa: F821
   assert major_color == ExpMajorColor, 'Detected Major color did not match with Expected Major color'
   assert minor_color == ExpMinorColor,'Detected Major color did not match with Expected Major color'

def testPairToNumber(major_color, minor_color, expected_pair_number):
   pair_number = getPairNumberFromColor(major_color, minor_color) # noqa: F821
   assert pair_number == expected_pair_number, 'Detected Major color did not match with Expected Major color'
     
if __name__ == '__main__':
  testNumberToPair(4, 'White', 'Red')
  testNumberToPair(5, 'White', 'Slate')
  testPairToNumber('Black', 'Orange', 12)
  testPairToNumber('Violet', 'Slate', 25)
  testPairToNumber('Red', 'Orange', 7)
  getColorNameAndPairNumber() # noqa: F821
  print('Done :')
