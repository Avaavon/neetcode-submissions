class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i,n in enumerate(nums):
            if i>0 and nums[i-1] == n:
                continue

            j = i+1
            k = len(nums) - 1
            while j<k:
                total = n + nums[j] + nums[k]
                if total>0:
                    k-=1
                elif total<0:
                    j+=1
                else:
                    res.append([n,nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1
        return res

# time: O(n^2)
# space: O(1) but if output included O(n^2)