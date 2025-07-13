class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for ind,i in enumerate(nums):
            product = 1
            for ind2,j in enumerate(nums):
                if ind2 != ind:
                    product *= j
            result.append(product)
        return result
    
# can be done with prefix and suffix product.
# do this later.
# [1,2,3,4]
# prefix = [1,1,2,6]
# suffix = [24,12,4,1]
# result = [24,12,8,6]

# [1,2,3,4,5]
# prefix = [1,1,2,6,24]
# suffix = [120,60,20,5,1]
# result = [120,60,40,30,24]