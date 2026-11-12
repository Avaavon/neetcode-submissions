class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # set a l and r pointer
        # mid = (r-l)/2
        l = 0
        r = len(nums) - 1

        while l<=r:
            mid = ((r-l)//2) + l
            if nums[mid] == target:
                return mid
            
            # if leftside sorted
            if nums[l] <= nums[mid]:
                # target inside it
                if nums[l]<= target < nums[mid]:
                    r = mid-1
                #target not inside
                else:
                    l = mid+1
            #rightside sorted
            else:
                #target inside
                if nums[mid]<target<=nums[r]:
                    l = mid+1
                else:
                    r = mid-1
        return -1