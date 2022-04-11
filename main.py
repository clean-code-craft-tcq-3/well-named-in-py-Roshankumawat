import ColorPair

def testNumberToPair(PairNumber, ExpMajorColor, ExpMinorColor):
   major_color, minor_color = getColorFromPairNumber(PairNumber) # noqa: F821
   assert major_color == ExpMajorColor, 'Detected Major color did not match with Expected Major color'
   assert minor_color == ExpMinorColor,'Detected Major color did not match with Expected Major color'

def testPairToNumber(major_color, minor_color, expected_pair_number):
   pair_number = getPairNumberFromColor(major_color, minor_color) # noqa: F821
   assert pair_number == expected_pair_number, 'Detected Major color did not match with Expected Major color'
     
if __name__ == '__main__':
  testPairToNumber('Violet', 'Slate', 25)
  testNumberToPair(4, 'White', 'Red')
  testNumberToPair(5, 'White', 'Slate')
  testPairToNumber('Black', 'Orange', 12)
  
  testPairToNumber('Red', 'Orange', 7)
  getColorNameAndPairNumber() # noqa: F821
  print('Done :')
