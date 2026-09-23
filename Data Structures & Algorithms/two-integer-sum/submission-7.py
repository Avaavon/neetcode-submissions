class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i,n in enumerate(nums):
            if target - n in seen:
                return [seen[target-n],i]
            else:
                seen[n] = i
    
# time: O(n) , for nums
# space: O(n), for the hash