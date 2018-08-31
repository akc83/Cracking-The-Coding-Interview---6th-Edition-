# Problem: Write a method to decide if two strings are anagrams or not.



# Solution:

def anagram(x,y):
  if len(x) != len(y):
    return False
  else:
    A = 0
    for char in x:
      if char in y:
        A+=1
  
  if A == len(x):
    return True
  else:
    return False



# Test Cases:
#    anagram('iceman','macein')
   
# => True
#    anagram('iceman','maceina')
   
# => False
#    anagram('iceman','maceii')