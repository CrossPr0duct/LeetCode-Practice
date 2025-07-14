
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # base case nothing
        if len(s) == 0:
            return False
        if len(s) == 1:
            return True

        # lowercase()
        s = s.lower()
        # remove anything non alphanumeric
        s = ''.join(char for char in s if char.isalnum())

        ptr1 = 0
        ptr2 = len(s)-1 # move to index space
        # need to know what happens when I divide and odd integer by 2 floor // drops the . decimal

        for i in range(len(s)): # range moves len(s) to index space already
            if s[ptr1] == s[ptr2]:
                if len(s) % 2 == 0: # even
                    if i == len(s)-1 // 2:
                        break
                elif len(s) % 2 == 1: # odd
                    if i == len(s)-1 // 2:
                        break
                ptr1 +=1
                ptr2 -=1
                continue
            else:
                return False

        return True

# [0,1,2] # len(s) = 3  => range(3) #odd
# [0,1,2,3] # len(s) = 4 => range(4) #even


