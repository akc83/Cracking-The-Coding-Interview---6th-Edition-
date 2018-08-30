# Problem: String Rotation: Assume you have a method isSubstring which checks if one word is a substring
#          of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one
#          call to isSubstring (e.g., waterbottle is a rotation of erbottlewat ).


# Solution: If we imagine that s2 is a rotation of s1, then we can ask what the rotation point is. For example, if you
#            rotate waterbottle after wat, you get erbottlewat. In a rotation, we cut s1 into two parts, x and y,
#            and rearrange them to get s2.
#            s1 = xy = waterbottle
#            x = wat
#            y = erbottle
#            s2 = yx = erbottlewat
#            So, we need to check if there's a way to split 51 into x and y such that xy = s1 and yx = s2. Regardless of
#            where the division between x and y is, we can see that yx will always bea substring of xyxy. That is, s2 will
#            always be a substring of s1s1.
#            And this is precisely how we solve the problem: simply do isSub5tring( s1s1, s2).


def rotation(s1, s2):
  if len(s1)==len(s2) and len(s1)>0: # making sure lengths of the strings are same and >0
    return isSubstring(s1s1, s2)

