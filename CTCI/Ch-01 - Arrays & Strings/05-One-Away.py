# Problem: One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bae -> false




# Solution:

def one_away(x,y):
  if len(x)>len(y):
    N = len(x)
  else:
    N = len(y)  # N is the length of the longer string
  
  count=0
  for char in x:
    if char in y:
      count+=1   # count is the number of characters that match in the two strings

  if count>=N-1:   # if only one or fewer (i.e., 0) characters are different in the two strings -> they are one step away
    return True
  else:
    return False





# Test Cases:
#    one_away('pale','ple')
   
# => True
#    one_away('pales','pale')
   
# => True
#    one_away('pales','bale')
   
# => False
#    one_away('pale','bale')
   
# => True
#    one_away('pale','bae')
   
# => False