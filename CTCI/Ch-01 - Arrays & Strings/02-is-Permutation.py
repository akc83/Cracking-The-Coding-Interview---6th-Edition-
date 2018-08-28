# Problem: Given two strings, write a method to decide if one is a permutation of the other.

# Solution

def permutation(x,y):
  if len(x)!=len(y):
    return False
  else:
    for letter in x:
      if letter not in y.lower() and letter not in y.upper():
        return False
        break
      else:
        return True
 


# Test Cases
#    permutation('dog','GOD')
   
# => True
#    permutation('DOG','god')
   
# => True
#    permutation('Dog','god')
   
# => True
#    permutation('aBCd','AbcD')
   
# => True
   