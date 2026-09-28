class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)


        prefix = 1
        i=0
        while i < len(nums):
            output[i] = prefix
            prefix *= nums[i]
            i+=1
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        
        return output

# time = O(n)
# space = O(n)