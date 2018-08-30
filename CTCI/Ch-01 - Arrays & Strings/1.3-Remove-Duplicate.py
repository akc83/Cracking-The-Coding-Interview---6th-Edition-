# Problem: Design an algorithm and write code to remove the duplicate characters in a string
#          without using any additional buffer. NOTE: One or two additional variables are fine.
#          An extra copy of the array is not.


# Solution:

def duplicate(string):
  A = list()
  for char in string:
    if char not in A:
      A.append(char)

  return ''.join(A)



# Test Cases:

#    duplicate('aabccd')
   
# => 'abcd'
#    duplicate('ababcdce')
   
# => 'abcde'