#  Problem: String Compression: Implement a method to perform basic string compression using the counts
#  of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
#  "compressed" string would not become smaller than the original string, your method should return
#  the original string. You can assume the string has only uppercase and lowercase letters (a - z).



# Solution:

def compression(string):
  L = list(string)
  c = 0
  
  x = list()

  for i in range(1,len(L)):
    if L[i]!=L[i-1]:           # if ith element is not the same as the (i-1)th element
      x.append(L[i-1])         # add (i-1)th element to the new list
      x.append(str(i-c))       # add i-c to the new list
      c = i
    
  x.append(L[i-1])             # finally add the last series of string and count
  x.append(str((i+1)-c))
    
  return ''.join(x)




# Test Cases:
#    compression('aabcccccaaa')
   
# => 'a2b1c5a3'
#    compression('aabbccddee')
   
# => 'a2b2c2d2e2'
#    compression('aabbaabbaabb')
   
# => 'a2b2a2b2a2b2'
#    compression('abcdabcd')
   
# => 'a1b1c1d1a1b1c1c1'
#    compression('abcdabcD')