class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_list=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j!=i:
                    if nums[j]+nums[i]==target:
                        new_list.append(i)
                        new_list.append(j)
                        return new_list