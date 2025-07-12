#Valid_Anagram.py

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

      # we want a time complexity where O(n + m) where n len s and m is len of t. 
      # we also want a space complexity that is constant.

      # base case lengths not the same we cannot have an anagram.
      if len(s) != len(t):
        return False

      # if we were to use a default dict there it would take k space.
      # assume that the strings are only characters.
      # constant space O(1) space, its a fixed size array
      space = [0] * 26

      # we know that the lens of the strings are the same
      # we can just loop over them without worrying about boundary conditions
      # so we want to know the character that maps to specific position
      base_unicode_num = ord('a')

      # now we want to balance the string using the unicode mapping each character to a position
      for a,b in zip(s,t):
        space[ord(a)-base_unicode_num] += 1
        space[ord(b)-base_unicode_num] -= 1
      # scan over the space and find that it is not 0 then it is not an anagram
      # otherwise it is.
      for i in space:
        if i != 0:
            return False

      return True
