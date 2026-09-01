class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMaps={}
        for index, value in enumerate(nums):
            diff=target-value
            if diff in prevMaps:
                return [prevMaps[diff],index]
            prevMaps[value]=index