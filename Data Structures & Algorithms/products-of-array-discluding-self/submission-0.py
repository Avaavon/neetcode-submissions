#Given an array of ints, return array of ints
#where output[i] is product of every num except for input[i]
#without division do O(n) time
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new_array=[1]*len(nums)

        for i in range(1,len(nums)):
            new_array[i]=new_array[i-1]*nums[i-1]

        right_products=1
        for j in range(len(nums)-1,0,-1):
            new_array[j-1]*=nums[j]*right_products
            right_products*=nums[j]
        return new_array
        
