from collections import defaultdict

class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # base case 
        if len(strs) == 0:
            return []

        if len(strs) == 1:
            return [[strs[0]]]

        final_result = defaultdict(list)

        for word in strs:
            str_hash = ''.join(sorted(word)) # sorted returns an list then we join it back.

            final_result[str_hash].append(word) 

        return list(final_result.values()) # values returns a list all the groups and we need it in a list form.

