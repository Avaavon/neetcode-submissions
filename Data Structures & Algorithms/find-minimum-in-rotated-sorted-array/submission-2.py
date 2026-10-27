class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        min_n = nums[0]

        while l <= r:
            # if sorted l to r
            if nums[l] < nums[r]:
                return min(nums[l], min_n)
            
            mid = (r+l) // 2
            # compare mid to min
            min_n = min(nums[mid], min_n)
            # if nums[mid] > nums[l] -> smallest on right (or min at l)
            if nums[mid] >= nums[l]:
                l = mid + 1
            # if nums[mid] < nums[l] -> smallest on left (or min at mid)
            else:
                r = mid - 1
        return min_n

