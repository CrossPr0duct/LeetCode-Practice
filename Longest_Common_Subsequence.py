class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        # create a set easily from a list.            
        s = set(nums)

        # weakness set operations...
        longest = -1
        
        # find the smallest number
        for num in s:
            if num - 1 not in s:
                # start counting

                current = num
                streak = 1

                while current + 1 in s:
                    current += 1
                    streak += 1

                longest = max(longest,streak)
        return longest