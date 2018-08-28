# Problem: Write a method to replace all spaces in a string with ‘%20’.

# Solution: 

def replace(string):
  string = (list(string))   # Important: string cannot be directly altered. Has to be converted to a list first.
  for i in range(len(string)):
    if string[i]==' ':
      string[i] = '%20'
  return ''.join(string)

      

# Test Cases:
#    replace('I am a boy')
   
# => 'I%20am%20a%20boy'
#    replace('I am a boy   ')
   
# => 'I%20am%20a%20boy%20%20%20'
#    replace('     He  SheHeHe ')
   
# => '%20%20%20%20%20He%20%20SheHeHe%20'