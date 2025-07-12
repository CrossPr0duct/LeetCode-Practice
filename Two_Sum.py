from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we want to add two numbers from the list to get the target.
        # output list that would provide indicies for the target.
        # don't sort the list array because it will break the code.

        # we want to do target - num = num2
        # we are asking what number must we pair with num ?

        # base case nothing return a empty list
        if len(nums) <= 0:
            return []

        if len(nums) == 2:
            return [0,1]

        seen = defaultdict(int)

        for i,num in enumerate(nums):
            item = target - num 
            
            if item in seen:
                firstPair = seen[item] 
                secondPair = i
                return [firstPair,secondPair]
            
            seen[num] = i
