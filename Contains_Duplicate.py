# Contains_Duplicate.py
from collections import defaultdict
# Done in 5 minutes.
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hist = defaultdict(int)

        for num in nums:
            hist[num] += 1

        
        for key in hist.keys():
            value = hist[key]

            if value >= 2:
                return True

        return False
