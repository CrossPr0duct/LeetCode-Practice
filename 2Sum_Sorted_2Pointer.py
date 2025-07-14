class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # base case
        # things the bounds check the bounds and ask about
        # whether there is a guarentee that one is returned.
        #  question was wrong requires that you return the ptr positions in non index space wtf.
        # effectively you want to binary search for the target. 
        ptr1 = 0
        ptr2 = len(numbers)-1
        pairFound = False
        if len(numbers) == 2:
            return [ptr1+1,ptr2+1]

        while pairFound == False:
            
            a = numbers[ptr1]
            b = numbers[ptr2]

            if a + b == target:
                return [ptr1+1,ptr2+1]

            elif a + b > target:
                ptr2 -= 1
            else:
                ptr1 += 1