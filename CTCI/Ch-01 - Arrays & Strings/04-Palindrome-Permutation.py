# Problem: Given a string, write a function to check if it is a permutation ofa palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

# EXAMPLE
# Input: Tact Coa
# Output: True (permutations:"taco cat'; "atco cta'; etc.)



# Solution:

# from collections import Counter -> a very hassle-free way. But below implementation does not use it.

def is_palindrome(string):
  L = list(string)
  d = dict()
  for item in L:
    if item!=' ': # proceed if the character is NOT an empty string
      if item.lower() not in d and item.upper() not in d:
        d[item.lower()] = 1
      elif item.lower() in d or item.upper() in d:
        d[item.lower()]+=1

  # return d -> just to check the dictionary it creates. it converts all chars to lower case and stores it
  
  count = 0
  for key in d:
    if d[key] % 2 != 0:
      count+=1            # increase the value of 'count' if any key's value is odd

  if count!=1:            # if count of more than one element is odd, then False, else True
    return False
  else:
    return True




# Test Cases:
#    is_palindrome('Tact Coa')
   
# => True
#    is_palindrome('tactcoapapa')
   
# => True
#    is_palindrome('taco cat')
   
# => True
#    is_palindrome('atco cta')
   
# => True
#    is_palindrome('atco ctao ')
   
# => False
#    is_palindrome('Tact CoA')
   
# => True
    



# Below is just a basic implementation to check if a string is a Palindrome. Not the same question though.

# def palindrome(string):
#   N = len(string)
#   i = 0
#   L = list()
#   while N>0:
#     L.insert(0,string[i]) 
#     N-=1
#     i+=1

#   if L == list(string):
#     return True
#   else:
#     return False 