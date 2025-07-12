from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hist = defaultdict(int)

        for num in nums:
            hist[num] += 1

        # sort by decending
        # need to get the hist as items which is {key:val}
        result = sorted(hist.items(),key=lambda x:x[1],reverse=True)
        return [x[0] for x in result[:k]]
