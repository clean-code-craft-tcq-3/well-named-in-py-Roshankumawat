import ColorPair

def testNumberToPair(pair_number,
                        expected_major_color, expected_minor_color):
  major_color, minor_color = getColorFromPairNumber(pair_number) # noqa: F821
  assert major_color == expected_major_color, 'Detected Major color did not match with Expected Major color'
  assert minor_color == expected_minor_color,'Detected Major color did not match with Expected Major color'

def testPairToNumber(major_color, minor_color, expected_pair_number):
  pair_number = getPairNumberFromColor(major_color, minor_color) # noqa: F821
  assert pair_number == expected_pair_number, 'Detected Major color did not match with Expected Major color'

if __name__ == '__main__':
  testNumberToPair(4, 'White', 'Red')
  testNumberToPair(5, 'White', 'Slate')
  testPairToNumber('Black', 'Orange', 12)
  testPairToNumber('Violet', 'Slate', 25)
  testPairToNumber('Red', 'Orange', 7)
  getColorNameAndPairNumber()
  print('Done :')
