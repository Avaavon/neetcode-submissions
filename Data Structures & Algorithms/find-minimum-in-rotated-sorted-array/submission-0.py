class Solution:
    def findMin(self, nums: List[int]) -> int:
        start=0
        end=len(nums)-1
        min_value=float('inf')

        if nums[start]<nums[end]:
            return nums[start]
        else:
            while start<=end:
                mid=start+((end-start)//2)
                min_value=min(min_value,nums[mid])

                if nums[mid]>nums[end]:
                    start=mid+1
                else:
                    end=mid-1
        return min_value
                    


