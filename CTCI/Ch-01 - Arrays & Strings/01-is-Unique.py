def contains_no_duplicates(string):
  letters = ''
  for letter in string:
    if letter not in letters:
      letters += letter
      
  if letters==string:
      return True
  else:
      return False



#  Test cases:     
#   contains_no_duplicates('abcd')
   
# => True
#    contains_no_duplicates('abcda')
   
# => False
#    contains_no_duplicates('abcdefgh')
   
# => True
#    contains_no_duplicates('abcdabcd')
      
# => False